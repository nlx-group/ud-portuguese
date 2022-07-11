#! /usr/bin/env python3

import logging
import transformers
import lxcommon


__version__ = "0.1.0"


LOGGER = logging.getLogger(__name__)


class PretokenizedTokenClassificationPipeline(transformers.TokenClassificationPipeline):
    def _sanitize_parameters(self, is_split_into_words=None, ignore_labels=None):
        preprocess_params, forward_params, postprocess_params = {}, {}, {}
        if is_split_into_words is not None:
            preprocess_params["is_split_into_words"] = is_split_into_words
            postprocess_params["is_split_into_words"] = is_split_into_words
        if ignore_labels is not None:
            postprocess_params["ignore_labels"] = ignore_labels
        return preprocess_params, forward_params, postprocess_params

    def preprocess(self, sentence, is_split_into_words=True):
        # see
        # https://github.com/huggingface/transformers/blob/51d7ebf260104cdd10f4c8fee295f9dad53775a5/src/transformers/pipelines/token_classification.py#L191
        truncation = (
            True
            if self.tokenizer.model_max_length and self.tokenizer.model_max_length > 0
            else False
        )
        model_inputs = self.tokenizer(
            sentence,
            return_attention_mask=False,
            return_tensors=self.framework,
            truncation=truncation,
            return_special_tokens_mask=True,
            return_offsets_mapping=self.tokenizer.is_fast,
            # the following argument is the main reason why we need this class:
            is_split_into_words=is_split_into_words,
        )
        model_inputs["sentence"] = sentence
        return model_inputs

    def postprocess(self, model_outputs, is_split_into_words=True, ignore_labels=None):
        entities = super().postprocess(model_outputs, ignore_labels=ignore_labels)
        if not is_split_into_words:
            return entities
        # merge tokens that were together at the input
        merged_entities = []
        for e in entities:
            if e["start"] > 0:
                word_piece = e["word"]
                if isinstance(word_piece, list):
                    if len(word_piece) != 1:
                        LOGGER.warning(f"postprocess() got list {word_piece!r} where a string was expected")
                    word_piece = "".join(word_piece)
                if word_piece.startswith("##"):
                    word_piece = word_piece[2:]
                merged_entities[-1]["word"] += word_piece
            else:
                merged_entities.append(e)
        return merged_entities


class LxUTaggerException(Exception):
    pass


class LxUTagger:
    def __init__(self, lazy_load=True):
        self._tokenizer = None
        self._model = None
        self._pipeline = None
        if not lazy_load:
            self.tokenizer
            self.model
            self.pipeline

    @property
    def tokenizer(self):
        if self._tokenizer is None:
            LOGGER.info("Loading tokenizer...")
            self._tokenizer = transformers.BertTokenizerFast.from_pretrained(
                "model", return_offsets_mapping=True
            )
            LOGGER.info(
                f"Tokenizer loaded. Vocabulary size: {len(self.tokenizer.vocab)}"
            )
        return self._tokenizer

    @property
    def model(self):
        if self._model is None:
            LOGGER.info("Loading model...")
            self._model = transformers.BertForTokenClassification.from_pretrained(
                "model"
            )
            LOGGER.info("Model loaded.")
        return self._model

    @property
    def pipeline(self):
        if self._pipeline is None:
            LOGGER.info("Creating pipeline...")
            self._pipeline = PretokenizedTokenClassificationPipeline(
                model=self.model,
                tokenizer=self.tokenizer,
                task="pos",
                is_split_into_words=True,
            )
            LOGGER.info("Pipeline created.")
        return self._pipeline

    def tag_paragraph(self, paragraph):
        pipeline_input = [[token.form for token in sentence] for sentence in paragraph]
        plain_text = "\n".join([" ".join(sentence) for sentence in pipeline_input])
        LOGGER.info(f"Tagging paragraph: {plain_text}")
        if LOGGER.isEnabledFor(logging.DEBUG):
            LOGGER.debug(f"Pipeline input: {pipeline_input!r}")
        pipeline_output = self.pipeline(pipeline_input)
        if LOGGER.isEnabledFor(logging.DEBUG):
            LOGGER.debug(f"Pipeline output: {pipeline_output!r}")
        if len(pipeline_output) != len(pipeline_input) or list(
            map(len, pipeline_output)
        ) != list(map(len, pipeline_input)):
            LOGGER.error(
                "Pipeline input and output lengths are not the same:\n"
                f"input={pipeline_input!r}\n"
                f"output={pipeline_output!r}"
            )
            raise LxUTaggerException("Input and output lengths are not the same")
        for sentence, output_sentence in zip(paragraph, pipeline_output):
            for token, output_token in zip(sentence, output_sentence):
                token.upos = output_token["entity"]
        return paragraph

    def tag_sentence(self, sentence):
        return self.tag_paragraph(lxcommon.LxParagraph(sentence))[0]


if __name__ == '__main__':
    import sys
    import lxtokenizer
    tokenizer = lxtokenizer.LxTokenizer()
    tagger = LxUTagger()
    for line in sys.stdin:
        sentence = tokenizer.tokenize_raw_sentence(line)
        tagger.tag_sentence(sentence)
        for token in sentence:
            print(token.form, token.upos, sep="\t")
        print()
