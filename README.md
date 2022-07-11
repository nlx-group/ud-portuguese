# Universal Grammatical Dependencies for Portuguese

This repository contains the models and datasets described in the article titled "Universal Grammatical Dependencies for Portuguese with CINTIL Data, LX Processing and CLARIN support" presented in LREC 2022.


You have two choices to download the code and datasets:

1. clone this repository via Git

2. download zip files from the PORTULAN CLARIN repository:

* [CINTIL-UPos dataset](https://hdl.handle.net/21.11129/0000-000E-8B30-F)
* [CINTIL-UDep dataset](https://hdl.handle.net/21.11129/0000-000E-8B2E-3)
* [CINTIL-USuite dataset](https://hdl.handle.net/21.11129/0000-000F-327D-D)
* [LX-UTagger Transformer model](https://hdl.handle.net/21.11129/0000-000E-8B2F-2)
* [LX-UDParser NLP4J model](https://hdl.handle.net/21.11129/0000-000E-8B31-E) 
* [LX-USuite Transformer models](https://hdl.handle.net/21.11129/0000-000F-327C-E)

However, the recommended and easiest way to use LX-UTagger, LX-UDParser, and LX-USuite is from the PORTULAN CLARIN workbench:

* [LX-UTagger](https://portulanclarin.net/workbench/lx-utagger/)
* [LX-UDParser](https://portulanclarin.net/workbench/lx-udparser/)
* [LX-USuite](https://portulanclarin.net/workbench/lx-usuite/)

## Contents

The followind data is available in this repository:

* The directory [`cintil-upos`](./cintil-upos) contains the CINTIL-UPos - CINTIL corpus annotated with Universal POS tags. See [`cintil-upos/README.md`](./cintil-upos/README.md).
* The directory [`cintil-udep`](./cintil-udep) contains the CINTIL-UDep - CINTIL treebank annotated with Universal Dependencies. See [`cintil-udep/README.md`](./cintil-udep/README.md).
* The directory [`cintil-usuite`](./cintil-usuite) contains the CINTIL-USuite - CINTIL corpus annotated with Universal POS tags, lemmas and Universal features. See [`cintil-usuite/README.md`](./cintil-usuite/README.md).

The followind models are available in this repository:

* The directory [`lx-udparser`](./lx-udparser) contains the LX-UDParser NLP4J model.  See [`lx-udparser/README.md`](lx-udparser/README.md) for more information.
* The directory [`lx-utagger`](./lx-utagger) contains the LX-UTagger Transformer model.  See [`lx-utagger/README.md`](lx-utagger/README.md) for more information.
* The directory [`lx-usuite`](./lx-usuite) contains the LX-USuite code, which is a wrapper for three token classifiers (LX-UTagger, LX-UFeaturizer and LX-NeuralLemmatizer)  See [`lx-usuite/README.md`](lx-usuite/README.md) for more information.
* The directory [`lx-ufeaturizer`](./lx-ufeaturizer) contains the LX-UFeaturizer Transformer models.  See [`lx-ufeaturizer/README.md`](lx-ufeaturizer/README.md) for more information.
* The directory [`lx-neurallemmatizer`](./lx-neurallemmatizer) contains the LX-NeuralLemmatizer Transformer models.  See [`lx-neurallemmatizer/README.md`](lx-neurallemmatizer/README.md) for more information.


## Publications

Irrespective of the most recent version of this dataset you may use, when mentioning it, please cite this reference:

António Branco, João Ricardo Silva, Luís Gomes and João Rodrigues, 2022, "Universal Grammatical Dependencies for Portuguese with CINTIL Data, LX Processing and CLARIN support", In Proceedings, 13th Conference on Language Resources and Evaluation (LREC2022) ([pdf](http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.603.pdf)).

Bibtex:

    @InProceedings{branco-EtAl:2022:LREC,
    author    = {Branco, António  and  Silva, João Ricardo  and  Gomes, Luís  and  António Rodrigues, João},
    title     = {Universal Grammatical Dependencies for Portuguese with CINTIL Data, LX Processing and CLARIN support},
    booktitle      = {Proceedings of the Language Resources and Evaluation Conference},
    month          = {June},
    year           = {2022},
    address        = {Marseille, France},
    publisher      = {European Language Resources Association},
    pages     = {5617--5626},
    url       = {https://aclanthology.org/2022.lrec-1.603}
    }

## License

The models and datasets in this repository are made available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

See [`LICENSE.txt`](./LICENSE.txt) for full text.

