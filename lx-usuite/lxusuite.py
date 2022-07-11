#! /usr/bin/env python3

from lxcommon import LxParagraph, LxSentence
from lxtokenizer import LxTokenizer

import wsgirpc


class LxUSuite:
    def __init__(
        self,
        lxneurallemmatizer_wsgirpc_url="http://lxneurallemmatizer-wsgirpc:8000",
        lxutagger_wsgirpc_url="http://lxutagger-wsgirpc:8000",
        lxufeaturizer_wsgirpc_url="http://lxufeaturizer-wsgirpc:8000",
    ):
        self.tokenizer = LxTokenizer()
        self.lemmatizer = wsgirpc.Proxy(lxneurallemmatizer_wsgirpc_url)
        self.tagger = wsgirpc.Proxy(lxutagger_wsgirpc_url)
        self.featurizer = wsgirpc.Proxy(lxufeaturizer_wsgirpc_url)

    def close(self):
        self.tokenizer.close()
        self.lemmatizer = None
        self.tagger = None
        self.featurizer = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def analyse_paragraph(self, paragraph, tag=None, lemmatize=None, featurize=None):
        if not isinstance(paragraph, LxParagraph):
            raise TypeError("paragraph must be an instance of LxParagraph")
        tag, lemmatize, featurize = self._check_options(tag, lemmatize, featurize)
        for sentence in paragraph:
            self.analyse_sentence(
                sentence, tag=tag, lemmatize=lemmatize, featurize=featurize
            )
        return paragraph

    def analyse_raw_sentence(
        self, raw_sentence, tag=None, lemmatize=None, featurize=None
    ):
        if not isinstance(raw_sentence, str):
            raise TypeError("raw_sentence must be str")
        return self.analyse_sentence(
            LxSentence(raw=raw_sentence),
            tag=tag,
            lemmatize=lemmatize,
            featurize=featurize,
        )

    def analyse_sentence(self, sentence, tag=None, lemmatize=None, featurize=None):
        if not isinstance(sentence, LxSentence):
            raise TypeError("sentence must be an instance of LxSentence")
        tag, lemmatize, featurize = self._check_options(tag, lemmatize, featurize)
        if not sentence.tokenized:
            self.tokenizer.tokenize_sentence(sentence)
        if tag:
            tagged_sentence = self.tagger.tag_sentence(sentence)
            for token, tagged_token in zip(sentence, tagged_sentence):
                token.upos = tagged_token.upos
        if lemmatize:
            lemmatized_sentence = self.lemmatizer.lemmatize_sentence(sentence)
            for token, lemmatized_token in zip(sentence, lemmatized_sentence):
                if isinstance(lemmatized_token.lemma, str):
                    token.lemma = lemmatized_token.lemma.upper()
                else:
                    token.lemma = lemmatized_token.lemma
        if featurize:
            featurized_sentence = self.featurizer.featurize_sentence(sentence)
            for token, featurized_token in zip(sentence, featurized_sentence):
                token.ufeats = featurized_token.ufeats
        return sentence

    def _check_options(self, tag, lemmatize, featurize):
        if tag is None:
            tag = True  # True by default
        if lemmatize is None:
            lemmatize = True  # True by default
        if featurize is None:
            featurize = True  # True by default
        return tag, lemmatize, featurize


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        usage = [
            f"usage: {sys.argv[0]} LEMMA_URL TAGGER_URL FEAT_URL < INPUTFILE > OUTPUTFILE",
            "where:"
            "LEMMA_URL is the URL of the LX-NeuralLemmatizer WSGI-RPC server;",
            "TAGGER_URL is the URL of the LX-UTagger WSGI-RPC server;",
            "FEAT_URL is the URL of the LX-UFeaturizer WSGI-RPC server;",
            "INPUTFILE is the path of a plain text file;",
            "OUTPUTFILE is the path of the output file, which will be in TSV format with",
            "           4 columns: form, lemma, pos, feats;",
            "           Sentences are separated with empty lines.",
        ]
        print(*usage, sep="\n", file=sys.stderr)
        sys.exit(2)

    (
        lxneurallemmatizer_wsgirpc_url,
        lxutagger_wsgirpc_url,
        lxufeaturizer_wsgirpc_url,
    ) = sys.argv[1:]

    usuite = LxUSuite(
        lxneurallemmatizer_wsgirpc_url,
        lxutagger_wsgirpc_url,
        lxufeaturizer_wsgirpc_url,
    )
    for line in sys.stdin:
        sentence = usuite.analyse_raw_sentence(line)
        for token in sentence:
            print(token.form, token.lemma, token.upos, token.ufeats, sep="\t")
        print()
