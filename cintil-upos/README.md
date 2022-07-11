# CINTIL-UPos - CINTIL dataset annotated with Universal POS tags

This dataset results from merging the CINTIL Treebank with the CINTIL Corpus.

Files are in TSV format (tab-separated values) with two columns: tokens and UPOS tags.
Sentences are separated with empty lines.

The file `cintil-upos-contracted.tsv` contains text as it normally appears in written form, with certain expressions in contracted form, such as "do" which results from the contraction of preposition "de" with definite article "o".  This is the dataset that was used to train the LX-UTagger.

The file `cintil-upos.tsv` contains the same text but with expanded contractions.
This tokenization conforms to the [CINTIL annotation guidelines](http://www.di.fc.ul.pt/~ahb/pubs/2005BarretoBrancoMendesEtAl.pdf).

Note that the two columns in these tsv files is identical to the first and third columns of the corresponding tsv files in the `../lx-usuite/` directory.


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

## Download

The most recent version of this dataset may be downloaded from [the PORTULAN CLARIN repository](https://hdl.handle.net/21.11129/0000-000E-8B30-F) or from [the nlx-group/ud-portuguese github repository](https://github.com/nlx-group/ud-portuguese).


## License

CINTIL-UPos is available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

See [`LICENSE.txt`](./LICENSE.txt) for full text.
