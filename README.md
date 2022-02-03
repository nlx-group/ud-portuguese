# Universal Grammatical Dependencies for Portuguese

This repository contains the models and datasets described in the article titled "Universal Grammatical Dependencies for Portuguese" submitted to LREC 2022.

You have two choices to download the code and datasets:

1. clone this repository via Git

2. download zip files from the PORTULAN CLARIN repository:

* [CINTIL-UPos dataset](https://hdl.handle.net/21.11129/0000-000E-8B30-F)
* [CINTIL-UDep dataset](https://hdl.handle.net/21.11129/0000-000E-8B2E-3)
* [LX-UTagger Transformer model](https://hdl.handle.net/21.11129/0000-000E-8B2F-2)
* [LX-UDParser NLP4J model](https://hdl.handle.net/21.11129/0000-000E-8B31-E) 

However, the recommended and easiest way to use LX-UTagger and LX-UDParser is from the PORTULAN CLARIN workbench:

* [LX-UTagger](https://portulanclarin.net/workbench/lx-utagger/)
* [LX-UDParser](https://portulanclarin.net/workbench/lx-udparser/)

## CINTIL-UPos - CINTIL corpus annotated with Universal POS tags

The directory `cintil-upos` contains the CINTIL-UPos dataset.

The directory contains two files in TSV format (tab-separated values) with two columns: tokens and UPOS tags.
Sentences are separated with empty lines.

The file `cintil-contracted-upos.tsv` contains text as it normally appears in written form, with certain expressions in contracted form, such as "do" which results from the contraction of preposition "de" with definite article "o".  This is the dataset that was used to train the LX-UTagger.

The file `cintil-upos.tsv` contains the same text but with expanded contractions.
This tokenization conforms to the [CINTIL annotation guidelines](http://www.di.fc.ul.pt/~ahb/pubs/2005BarretoBrancoMendesEtAl.pdf).

## CINTIL-UDep - CINTIL treebank annotated with Universal Dependencies

The directory `cintil-udep` contains the CINTIL-UDep treebank.
This treebank contains 37780 sentences and 473929 tokens.

The file `cintil-udep.conll` in CONLL format, which is a TSV format (tab-separated values) with 10 columns: token id, form, lemma, cpos, pos, feat, head, deprel, phead, pdeprel.
Sentences are separated with empty lines.  Note that both the POS and dependencies in this file are manually validated.  The LX-UDParser was trained on a derivative of this file, where the POS annotations were made by the LX-UTagger, instead.

Lines starting with an hash (#) are comments.

The tokenization conforms to the [CINTIL annotation guidelines](http://www.di.fc.ul.pt/~ahb/pubs/2005BarretoBrancoMendesEtAl.pdf).

# LX-UTagger

The directory `lx-utagger` contains the LX-UTagger.

This tagger is based on the [BERTimbau pre-trained BERT model](https://github.com/neuralmind-ai/portuguese-bert) and has been fined tuned on the CINTIL-UPos dataset.

The model files are contained in the directory `lx-utagger/model`.

Please download and install Python (>=3.7), and then install required packages with the command `pip install -r requirements.txt` (assuming the current directory is `lx-utagger`).

After installation, you may run LX-UTagger with the following command:

    python lxutagger.py < INPUTFILE > OUTPUTFILE

Replace INPUTFILE and OUTPUTFILE with the appropriate file names.  The input format is plain text with one sentence per line.
The output format is TSV (tab-separated-values) with two columns: token and UPOS.

# LX-UDParser

The directory `lx-udparser` contains the LX-UDParser.

This parser is currently based on the NLP4J dependency parser and the model provided in this repository was trained on the CINTIL-UDep dataset.

The NLP4J model file is named `nlp4j-model-lxudparser.xz`.
The file named `nlp4j-model-lxudparser-config.xml` is a XML configuration needed for running NLP4J.

Please download and install NLP4J, following instructions from https://github.com/emorynlp/nlp4j.

After installation, you may run NLP4J with the following command:

    nlpdecode -c nlp4j-model-lxudparser-config.xml -format tsv -oe annotated -i INPUTFILE

The configuration file assumes that the model file resides in the same directory from where the `nlpdecode` command will be executed.  If you get an error, try changing the model file path to an absolute path.

Replace INPUTFILE with the appropriate file name.  The input format is TSV (tab-separated-values) with four columns: form, lemma, UPOS, features.
This model was trained on texts annotated by LX-UTagger, and thus for the best performance we recommend to use LX-UTagger to annotate the input texts.

## License

The models and datasets in this repository are made available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

See LICENSE.txt for full text.

