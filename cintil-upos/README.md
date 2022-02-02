# CINTIL-UPos - CINTIL corpus annotated with Universal POS tags

Files are in TSV format (tab-separated values) with two columns: tokens and UPOS tags.
Sentences are separated with empty lines.

The file `cintil-contracted-upos.tsv` contains text as it normally appears in written form, with certain expressions in contracted form, such as "do" which results from the contraction of preposition "de" with definite article "o".  This is the dataset that was used to train the LX-UTagger.

The file `cintil-upos.tsv` contains the same text but with expanded contractions.
This tokenization conforms to the [CINTIL annotation guidelines](http://www.di.fc.ul.pt/~ahb/pubs/2005BarretoBrancoMendesEtAl.pdf).

## License

CINTIL-UPos is available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

See `../LICENSE.txt` for full text.
