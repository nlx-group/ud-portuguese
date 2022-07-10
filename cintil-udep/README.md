# CINTIL-UDep - CINTIL Universal Dependencies treebank

The CINTIL-UDep treebank contains 37780 sentences and 473929 tokens.

The file `cintil-udep.conll` in CONLL format, which is a TSV format (tab-separated values) with 10 columns: token id, form, lemma, cpos, pos, feat, head, deprel, phead, pdeprel.
Sentences are separated with empty lines.  Note that both the POS and dependencies in this file are manually validated.  The LX-UDParser was trained on a derivative of this file, where the POS annotations were made by the LX-UTagger, instead.

Lines starting with an hash (#) are comments.

The tokenization conforms to the [CINTIL annotation guidelines](http://www.di.fc.ul.pt/~ahb/pubs/2005BarretoBrancoMendesEtAl.pdf).

## License

CINTIL-UDep is available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

See `LICENSE.txt` for full text.
