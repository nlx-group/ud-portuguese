#! /usr/bin/env python3

import lxtokenizer
import wsgirpc
import sys

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} URL < INPUTFILE > OUTPUTFILE", file=sys.stderr)
    sys.exit(2)
else:
    url = sys.argv[1]  # e.g. http://localhost:8000

tagger = wsgirpc.Proxy(url)
print(f"Connected to LX-UTagger version {tagger.version()} on {url}", file=sys.stderr)


tokenizer = lxtokenizer.LxTokenizer()
for line in sys.stdin:
    sentence = tokenizer.tokenize_raw_sentence(line)
    sentence = tagger.tag_sentence(sentence)
    for token in sentence:
        print(token.form, token.upos, sep="\t")
    print()
