# LX-USuite

LX-USuite is a tool composed of three token classifiers:
* LX-UTagger (Universal POS tagger)
* LX-UFeaturizer (Universal featurizer)
* LX-NeuralLemmatizer

Each of these classifiers is based on the [BERTimbau pre-trained BERT model](https://github.com/neuralmind-ai/portuguese-bert) and has been fined tuned on the companion CINTIL-USuite dataset, available [from the PORTULAN CLARIN repository](https://hdl.handle.net/21.11129/0000-000F-327D-D) or from [the nlx-group/ud-portuguese github repository](https://github.com/nlx-group/ud-portuguese).

The models and code for each of the three classifiers is organized in separate directories:
* [`../lx-utagger`](../lx-utagger/) for the LX-UTagger,
* [`../lx-ufeaturizer`](../lx-ufeaturizer/) for the LX-UFeaturizer,
* and [`../lx-neurallemmatizer`](../lx-neurallemmatizer/) for the LX-NeuralLemmatizer.

Please refer to the `README.md` file within each directory for information on how to pull, build and run the Docker images of these classifiers.

## Running LX-USuite

To run LX-USuite, there are several options, described below.

### Run LX-USuite on the PORTULAN CLARIN workbench (most recommended)

This option is recommended because it has the least requirements: only a web browser is needed.

The following access modes are offered at https://portulanclarin.net/workbench/lx-usuite :
* direct text-input interface for processing short texts;
* file-processing interface for larger texts;
* web services for integrating LX-USuite in your code;
* Jupyter notebooks for exploratory learning.

### Run LX-USuite components on Docker containers (recommended)

This option is recommended because it avoids dealing with installation of a huge number of Python packages for the components (LX-UTagger, LX-UFeaturizer and LX-NeuralLemmatizer).

Pre-built images for each component are available from Docker hub. Please see the `README.md` file within the directory of each component for guidance.

Assuming Python (>=3.7) is installed, run this command to install required packages: `pip install -r requirements.txt`.

After WSGI-RPC servers for the three components are setup and running on Docker containers, LX-USuite can be used to analyse a plain text file as follows (Bash syntax):


    TAGGER_URL="http://localhost:8000"
    LEMMA_URL="http://localhost:8001"
    FEAT_URL="http://localhost:8002"

    ./lxusuite $LEMMA_URL $TAGGER_URL $FEAT_URL < INPUTFILE > OUTPUTFILE

Where:

* the `TAGGER_URL` variable contains the URL of the LX-UTagger WSGI-RPC server,
* the `LEMMA_URL` variable contains the URL of the LX-NeuralLemmatizer WSGI-RPC server,
* the `FEAT_URL` variable contains the URL of the LX-UFeaturizer WSGI-RPC server,
* `INPUTFILE` is the path of a plain text file with one sentence per line,
* and `OUTPUTFILE` is the path of the output TSV file, which will contain four columns per token:
    1. the token form,
    1. the lemma,
    1. the UPOS tag
    1. and Universal features bundle.
An empty line denotes the end of a sentence.


## Publications

Irrespective of the most recent version of this tagger you may use, when mentioning it, please cite this reference:

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

The most recent version of this tagger may be downloaded from [the PORTULAN CLARIN repository](https://hdl.handle.net/21.11129/0000-000E-8B2F-2) or from [the nlx-group/ud-portuguese github repository](https://github.com/nlx-group/ud-portuguese).


## License

The models and code in this repository are made available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

See `LICENSE.txt` for full text.

