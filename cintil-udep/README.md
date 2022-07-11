# CINTIL-UDep - CINTIL Universal Dependencies treebank

The CINTIL-UDep treebank contains 37780 sentences and 473929 tokens.

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


## Publications

Irrespective of the most recent version of this treebank you may use, when mentioning it, please cite this reference:

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

The most recent version of this treebank may be downloaded from [the PORTULAN CLARIN repository](https://hdl.handle.net/21.11129/0000-000E-8B2E-3) or from [the nlx-group/ud-portuguese github repository](https://github.com/nlx-group/ud-portuguese).


## License

CINTIL-UDep is available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

See `LICENSE.txt` for full text.
