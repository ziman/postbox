#!/usr/bin/env python3

import os
import flask
import logging
import argparse

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
app = flask.Flask(__name__)

UPLOAD_ROOT = os.path.realpath('./uploads/')

@app.route("/upload/<path:path>", methods=['POST'])
def hello(path):
    fullpath = os.path.realpath(
        os.path.join(UPLOAD_ROOT, path)
    )

    if not fullpath.startswith(UPLOAD_ROOT):
        flask.abort(403)  # forbidden

    if os.path.exists(fullpath):
        flask.abort(409)  # conflict

    flask.request.files['file'].save(fullpath)

    return 'ok'
