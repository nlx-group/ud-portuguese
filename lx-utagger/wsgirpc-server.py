#! /usr/bin/env python3

import wsgirpc
import lxutagger

NINSTANCES = 2
LAZY_LOAD = True


class LxUTagger(lxutagger.LxUTagger):
    def version(self):
        return lxutagger.__version__


app = wsgirpc.Server([LxUTagger(lazy_load=LAZY_LOAD) for _ in range(NINSTANCES)])


if __name__ == "__main__":
    import logging.config
    from wsgiref.simple_server import make_server

    logging.config.fileConfig("logging.conf")

    with make_server("0.0.0.0", 8000, app) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
