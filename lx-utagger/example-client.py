#! /usr/bin/env python3

import lxcommon
import wsgirpc
import sys

if len(sys.argv) > 2:
    print(f"usage: {sys.argv[0]} [url]", file=sys.stderr)
    sys.exit(2)
elif len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = "http://localhost:8000"

tagger = wsgirpc.Proxy(url)
print(f"getting version from LX-UTagger wsgi server: {tagger.version()}")


text = """
Esta frase serve para testar o funcionamento do LX-UTagger. Esta outra frase faz o mesmo.
"""

paragraph = [
    line.split() for line in text.splitlines() if line.strip()
]

paragraph = lxcommon.LxParagraph.from_primitive_types([
    [{"form": form} for form in sentence]
    for sentence in paragraph
])

print("\nForm\tUPOS:\n")
paragraph = tagger.tag_paragraph(paragraph)
for sentence in paragraph:
    for token in sentence:
        print(token.form, token.upos, sep="\t")
    print()
