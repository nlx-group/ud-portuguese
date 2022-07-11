# Universal Grammatical Dependencies for Portuguese

This repository contains the models and datasets described in the article titled "Universal Grammatical Dependencies for Portuguese with CINTIL Data, LX Processing and CLARIN support" presented in LREC 2022.


You have two choices to download the code and datasets:

1. clone this repository via Git

2. download zip files from the PORTULAN CLARIN repository:

* [CINTIL-UPos dataset](https://hdl.handle.net/21.11129/0000-000E-8B30-F)
* [CINTIL-UDep dataset](https://hdl.handle.net/21.11129/0000-000E-8B2E-3)
* [CINTIL-USuite dataset]()
* [LX-UTagger Transformer model](https://hdl.handle.net/21.11129/0000-000E-8B2F-2)
* [LX-UDParser NLP4J model](https://hdl.handle.net/21.11129/0000-000E-8B31-E) 
* [LX-USuite models]()

However, the recommended and easiest way to use LX-UTagger and LX-UDParser is from the PORTULAN CLARIN workbench:

* [LX-UTagger](https://portulanclarin.net/workbench/lx-utagger/)
* [LX-UDParser](https://portulanclarin.net/workbench/lx-udparser/)
* [LX-USuite](https://portulanclarin.net/workbench/lx-usuite/)

## CINTIL-UPos - CINTIL corpus annotated with Universal POS tags

The directory `cintil-upos` contains the CINTIL-UPos dataset.

The directory contains two files in TSV format (tab-separated values) with two columns: tokens and UPOS tags.
Sentences are separated with empty lines.

The file `cintil-contracted-upos.tsv` contains text as it normally appears in written form, with certain expressions in contracted form, such as "do" which results from the contraction of preposition "de" with definite article "o".  This is the dataset that was used to train the LX-UTagger.

Sample sentence:

    A           DET
    encomenda   NOUN
    está        VERB
    no          ADP+DET
    armazém     NOUN
    .           PUNCT
    

The file `cintil-upos.tsv` contains the same text but with expanded contractions.

Sample sentence:

    A           DET
    encomenda   NOUN
    está        VERB
    em_         ADP
    o           DET
    armazém     NOUN
    .           PUNCT

This tokenization conforms to the [CINTIL annotation guidelines](http://www.di.fc.ul.pt/~ahb/pubs/2005BarretoBrancoMendesEtAl.pdf).

## CINTIL-UDep - CINTIL treebank annotated with Universal Dependencies

The directory `cintil-udep` contains the CINTIL-UDep treebank.
This treebank contains 37780 sentences and 473929 tokens.

The file `cintil-udep.conllu` in CONLL-U format, which is a TSV format (tab-separated values) with 10 columns:

1. ID: Word index, integer starting at 1 for each new sentence; may be a range for multiword tokens; may be a decimal number for empty nodes (decimal numbers can be lower than 1 but must be greater than 0).
2. FORM: Word form or punctuation symbol.
3. LEMMA: Lemma of word form.
4. UPOS: Universal part-of-speech tag.
5. XPOS: Language-specific part-of-speech tag.
6. FEATS: List of morphological features from the universal feature inventory or from a defined language-specific extension; underscore if not available.
7. HEAD: Head of the current word, which is either a value of ID or zero (0).
8. DEPREL: Universal dependency relation to the HEAD (root iff HEAD = 0) or a defined language-specific subtype of one.
9. DEPS: Enhanced dependency graph in the form of a list of head-deprel pairs.
10. MISC: Any other annotation.

Sentences are separated with empty lines.  Note that both the POS and dependencies in this file are manually validated.  The LX-UDParser was trained on a derivative of this file, where the POS annotations were made by the LX-UTagger, instead.

See https://universaldependencies.org/format.html#conll-u-format for more details on the CONLL-U format.

Lines starting with an hash (#) are comments.

The tokenization conforms to the [CINTIL annotation guidelines](http://www.di.fc.ul.pt/~ahb/pubs/2005BarretoBrancoMendesEtAl.pdf).

## CINTIL-USuite - CINTIL corpus annotated with Universal POS tags, lemmas and Universal features

The directory `cintil-usuite` contains the CINTIL-USuite dataset.

The directory contains two files in TSV format (tab-separated values) with four columns: tokens, lemmas, UPOS tags and universal feature bundles.
Sentences are separated with empty lines.

The file `cintil-contracted-usuite.tsv` contains text as it normally appears in written form, with certain expressions in contracted form, such as "do" which results from the contraction of preposition "de" with definite article "o".  This is the dataset that was used to train the models underpinning LX-USuite, which include LX-UTagger, LX-UFeaturizer and LX-NeuralLemmatizer.

Sample sentence:

The file `cintil-usuite.tsv` contains the same text as `cintil-contracted-usuite.tsv` but with expanded contractions.

Sample sentence:


This tokenization conforms to the [CINTIL annotation guidelines](http://www.di.fc.ul.pt/~ahb/pubs/2005BarretoBrancoMendesEtAl.pdf).

# LX-UTagger

The directory `lx-utagger` contains the LX-UTagger.  See [`lx-utagger/README.md`](lx-utagger/README.md) for more information.

This tagger is based on the [BERTimbau pre-trained BERT model](https://github.com/neuralmind-ai/portuguese-bert) and has been fined tuned on the CINTIL-UPos dataset, available [from the PORTULAN CLARIN repository](https://hdl.handle.net/21.11129/0000-000E-8B30-F) or from [the nlx-group/ud-portuguese github repository](https://github.com/nlx-group/ud-portuguese).


# LX-UDParser

The directory `lx-udparser` contains the LX-UDParser.  See [`lx-udparser/README.md`](lx-udparser/README.md) for more information.

This parser is currently based on the NLP4J dependency parser and the model provided in this repository was trained on the CINTIL-UDep dataset.

## License

The models and datasets in this repository are made available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

Please cite this paper if you use any of the models or datasets in this repository:

    @InProceedings{branco-EtAl:2022:LREC,
        author    = {Branco, António  and  Silva, João Ricardo  and  Gomes, Luís  and  António Rodrigues, João},
        title     = {Universal Grammatical Dependencies for Portuguese with CINTIL Data, LX Processing and CLARIN support},
        booktitle = {Proceedings of the Language Resources and Evaluation Conference},
        month     = {June},
        year      = {2022},
        address   = {Marseille, France},
        publisher = {European Language Resources Association},
        pages     = {5617--5626},
        url       = {https://aclanthology.org/2022.lrec-1.603}
    }

See LICENSE.txt for full text.

