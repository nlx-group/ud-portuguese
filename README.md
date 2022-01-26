# Universal Grammatical Dependencies for Portuguese

This repository contains the models and datasets described in the article titled "Universal Grammatical Dependencies for Portuguese" submitted to LREC 2022.

You have two choices to download the code and datasets:

1. clone this repository via Git

2. download zip files from the PORTULAN CLARIN repository:

    * [CINTIL-UPos dataset](https://portulanclarin.net/repository/browse/cintil-upos/3aeee0ba7d2511ec93d302420a87011b71d1cce08e0e4689a3ce96b6fda67312/)
    * [CINTIL-UDep dataset](https://portulanclarin.net/repository/browse/cintil-udep/323c45107e3e11ec93d302420a87011b333aff3eeebc4e6abde8e2df8505315c/)
    * LX-UPosTagger (Transformer) model (comming soon)
    * [LX-UDepParser NLP4J model](https://portulanclarin.net/repository/browse/lx-udepparser/5ae6058c7e3911ec93d302420a87011b50a034a1eb0e47a5988a0b2326f50372/) 

## CINTIL-UPos

The directory `cintil-upos` contains the CINTIL-UPos dataset.

The directory contains two files in TSV format (tab-separated values) with two columns: tokens and UPOS tags.
Sentences are separated with empty lines.

The file `cintil-contracted-upos.tsv` contains text as it normally appears in written form, with certain expressions in contracted form, such as "do" which results from the contraction of preposition "de" with definite article "o".  This is the dataset that was used to train the LX-UPos tagger.

The file `cintil-upos.tsv` contains the same text but with expanded contractions.
This tokenization conforms to the [CINTIL annotation guidelines](http://www.di.fc.ul.pt/~ahb/pubs/2005BarretoBrancoMendesEtAl.pdf).

## CINTIL-UDep

The directory `cintil-udep` contains the CINTIL-UDep treebank.

The directory contains the file `cintil-udep.conll` in CONLL format, which is a TSV format (tab-separated values) with 10 columns: token id, form, lemma, cpos, pos, feat, head, deprel, phead, pdeprel.
Sentences are separated with empty lines.  Note that both the POS and dependencies in this file are manually validated.  The LX-UdepParser was trained on a derivative of this file, where the POS annotations were made by the LX-UPosTagger, instead.

Lines starting with an hash (#) are comments.

The tokenization conforms to the [CINTIL annotation guidelines](http://www.di.fc.ul.pt/~ahb/pubs/2005BarretoBrancoMendesEtAl.pdf).


## License

The models and datasets in this repository are made available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

See LICENSE.txt for full text.

