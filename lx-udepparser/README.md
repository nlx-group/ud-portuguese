# LX-UDepParser

LX-UDepParser is currently based on the NLP4J dependency parser and the model provided in this repository was trained on the CINTIL-UDeps dataset.

The NLP4J model file is named `nlp4j-model-lxdepparser.xz`.
The file named `nlp4j-model-lxdepparser-config.xml` is a XML configuration needed for running NLP4J.

Please download and install NLP4J, following instructions from https://github.com/emorynlp/nlp4j.

After installation, you may run NLP4J with the following command:

    nlpdecode -c nlp4j-model-lxdepparser-config.xml -format tsv -oe annotated -i INPUTFILE

The configuration file assumes that the model file resides in the same directory from where the `nlpdecode` command will be executed.  If you get an error, try changing the model file path to an absolute path.

Replace INPUTFILE with the appropriate file name.  The input format is TSV (tab-separated-values) with four columns: form, lemma, UPOS, features.
This model was trained on texts annotated by LX-UPosTagger, and thus for the best performance we recommend to use LX-UPosTagger to annotate the input texts.

## License

LX-UDepParser is available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

See LICENSE.txt for full text.

NLP4J is available under the Apache2 license.

See http://www.apache.org/licenses/LICENSE-2.0 for full text.

