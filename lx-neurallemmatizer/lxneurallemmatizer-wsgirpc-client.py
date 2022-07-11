#! /usr/bin/env python3

import lxtokenizer
import wsgirpc
import sys

if len(sys.argv) != 2:
    usage = [
        f"usage: {sys.argv[0]} LEMMA_URL < INPUTFILE > OUTPUTFILE",
        "where:"
        "LEMMA_URL is the URL of the LX-NeuralLemmatizer WSGI-RPC server;",
        "          e.g. http://localhost:8001",
        "INPUTFILE is the path of a plain text file;",
        "OUTPUTFILE is the path of the output file, which will be in TSV format with",
        "           2 columns: form, lemma;",
        "           Sentences are separated with empty lines.",
    ]
    print(*usage, sep="\n", file=sys.stderr)
    sys.exit(2)
else:
    url = sys.argv[1]

lemmatizer = wsgirpc.Proxy(url)
print(f"Connected to LX-NeuralLemmatizer version {lemmatizer.version()} on {url}", file=sys.stderr)


tokenizer = lxtokenizer.LxTokenizer()
for line in sys.stdin:
    sentence = tokenizer.tokenize_raw_sentence(line)
    sentence = lemmatizer.lemmatize_sentence(sentence)
    for token in sentence:
        print(token.form, token.lemma.upper(), sep="\t")
    print()
