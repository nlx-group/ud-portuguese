# Universal Grammatical Dependencies for Portuguese

This repository contains the models and datasets described in the article titled "Universal Grammatical Dependencies for Portuguese" submitted to LREC 2022.

You have two choices to download the code and datasets:

1. clone this repository via Git

2. download zip files from the PORTULAN CLARIN repository:

    * [CINTIL-UPos dataset](https://portulanclarin.net/repository/browse/cintil-upos/3aeee0ba7d2511ec93d302420a87011b71d1cce08e0e4689a3ce96b6fda67312/)
    * CINTIL-UDep dataset (comming soon)
    * LX-UPosTagger (Transformer) model (comming soon)
    * LX-UDepParser (NLP4J) model (comming soon)

## CINTIL-UPos

The directory `cintil-upos` contains the CINTIL-UPos dataset.

The directory contains two files in TSV format (tab-separated values) with two columns: tokens and UPOS tags.
Sentences are separated with empty lines.

The file `cintil-contracted-upos.tsv` contains text as it normally appears in written form, with certain expressions in contracted form, such as "do" which results from the contraction of preposition "de" with definite article "o".  This is the dataset that was used to train the LX-UPos tagger.

The file `cintil-upos.tsv` contains the same text but with expanded contractions.
This tokenization conforms to the [CINTIL annotation guidelines](http://www.di.fc.ul.pt/~ahb/pubs/2005BarretoBrancoMendesEtAl.pdf).
