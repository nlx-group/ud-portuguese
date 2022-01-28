# LX-UPosTagger

The directory `lx-upostagger` contains the LX-UPosTagger.

This tagger is based on the [BERTimbau pre-trained BERT model](https://github.com/neuralmind-ai/portuguese-bert) and has been fined tuned on the CINTIL-UPos dataset.

The model files are contained in the directory `lx-upostagger/model`.

Please download and install Python (>=3.7), and then install required packages with the command `pip install -r requirements.txt` (assuming the current directory is `lx-upostagger`).

After installation, you may run LX-UPosTagger with the following command:

    python lxupostagger.py < INPUTFILE > OUTPUTFILE

Replace INPUTFILE and OUTPUTFILE with the appropriate file names.  The input format is plain text with one sentence per line.
The output format is TSV (tab-separated-values) with two columns: token and UPOS.
## License

The models and code in this repository are made available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

See `../LICENSE.txt` for full text.

