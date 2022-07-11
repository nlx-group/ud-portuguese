#! /usr/bin/env python3

import wsgirpc
import lxneurallemmatizer

NINSTANCES = 2
LAZY_LOAD = True


class LxNeuralLemmatizer(lxneurallemmatizer.LxNeuralLemmatizer):
    def version(self):
        return lxneurallemmatizer.__version__


app = wsgirpc.Server(
    [LxNeuralLemmatizer(lazy_load=LAZY_LOAD) for _ in range(NINSTANCES)]
)


if __name__ == "__main__":
    import logging.config
    from wsgiref.simple_server import make_server

    logging.config.fileConfig("logging.conf")

    with make_server("0.0.0.0", 8000, app) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
