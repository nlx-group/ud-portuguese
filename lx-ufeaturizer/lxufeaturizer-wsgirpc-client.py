#! /usr/bin/env python3

import lxtokenizer
import wsgirpc
import sys

if len(sys.argv) != 2:
    usage = [
        f"usage: {sys.argv[0]} FEAT_URL < INPUTFILE > OUTPUTFILE",
        "where:"
        "FEAT_URL is the URL of the LX-UFeaturizer WSGI-RPC server;",
        "          e.g. http://localhost:8002",
        "INPUTFILE is the path of a plain text file;",
        "OUTPUTFILE is the path of the output file, which will be in TSV format with",
        "           2 columns: form, universal feature bundle;",
        "           Sentences are separated with empty lines.",
    ]
    print(*usage, sep="\n", file=sys.stderr)
    sys.exit(2)
else:
    url = sys.argv[1]

featurizer = wsgirpc.Proxy(url)
print(f"Connected to LX-UFeaturizer version {featurizer.version()} on {url}", file=sys.stderr)


tokenizer = lxtokenizer.LxTokenizer()
for line in sys.stdin:
    sentence = tokenizer.tokenize_raw_sentence(line)
    sentence = featurizer.featurize_sentence(sentence)
    for token in sentence:
        print(token.form, token.ufeats, sep="\t")
    print()
