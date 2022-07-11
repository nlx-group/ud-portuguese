# LX-NeuralLemmatizer

LX-NeuralLemmatizer is a tool for lemmatization of Portuguese words based on the [BERTimbau pre-trained BERT model](https://github.com/neuralmind-ai/portuguese-bert) and has been fined tuned on the CINTIL-USuite dataset, available [from the PORTULAN CLARIN repository](https://hdl.handle.net/21.11129/0000-000F-327D-D) or from [the nlx-group/ud-portuguese github repository](https://github.com/nlx-group/ud-portuguese).

The model files are contained in the directory `model`.

This model is an instance of the [BertForTokenClassification](https://huggingface.co/docs/transformers/master/model_doc/bert#transformers.BertForTokenClassification) model.
Refer to the [Transformers documentation](https://huggingface.co/docs/transformers/master/model_doc/bert) if you want to use this model in your own code and take a look at `lxneurallemmatizer.py`.

## Running LX-NeuralLemmatizer

To run LX-NeuralLemmatizer, there are two options, described below.

### Run LX-NeuralLemmatizer on a Docker container (recommended)

This option is recommended because it avoids dealing with installation of a huge number of Python packages.

A pre-built image is available from Docker hub.  Assuming that docker is already installed, to pull the pre-built image execute the commands `docker pull luismsgomes/lxneurallemmatizer:latest` and `docker tag luismsgomes/lxneurallemmatizer:latest lxneurallemmatizer:latest`.

Alternatively, to build the docker image, assuming docker is already installed, execute the command `docker build --tag lxneurallemmatizer:latest`.

By default, running this image will start a WSGI-RPC server, which can be accessed via sockets as shown in `lxneurallemmatizer-wsgirpc-client.py`.
To start the docker container, execute the command: `docker run --rm --detach --name lxneurallemmatizer --publish 8001:8000 lxneurallemmatizer:latest`.

Then, to communicate with the WSGI-RPC server running on the container, assuming Python (>=3.7) is already installed, a couple of packages need to be installed:

    pip install -r requirements-client.txt

Then, run `./lxneurallemmatizer-wsgirpc-client.py http://localhost:8001 < INPUTFILE > OUTPUTFILE`, where `INPUTFILE` is a plain text file with one sentence per line, and `OUTPUTFILE` will be a TSV file, with two columns: token form and lemma.  End of a sentence is marked with an empty line.

To stop the container, run `docker stop lxneurallemmatizer`.

### Run LX-NeuralLemmatizer directly

Install Python (>=3.7) and the required packages from `requirements.txt`.  Use of a virtualenv is highly recommended because Pytorch will pull many dependency packages.

To run the lemmatizer use the command: `./lxneurallemmatizer.py < INPUTFILE > OUTPUTFILE`, where `INPUTFILE` is a plain text file with one sentence per line, and `OUTPUTFILE` will be a TSV file, with two columns: token form and lemma.  End of a sentence is marked with an empty line.


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

The most recent version of this model may be downloaded from [the PORTULAN CLARIN repository](https://hdl.handle.net/21.11129/0000-000E-8B2F-2) or from [the nlx-group/ud-portuguese github repository](https://github.com/nlx-group/ud-portuguese).


## License

The models and code in this repository are made available under the Creative Commons BY-NC-ND license (Attribution-NonCommercial-NoDerivatives 4.0 International).

See `LICENSE.txt` for full text.

