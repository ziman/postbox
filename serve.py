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

    os.makedirs(os.path.dirname(fullpath), exist_ok=True)
    flask.request.files['file'].save(fullpath)

    return 'ok'

@app.route("/")
def home():
    return \
        '<html>' \
        '<form action="/upload/somefile" method="post" enctype="multipart/form-data">' \
        '<input type="file" name="file" />' \
        '<input type="submit" />' \
        '</form>' \
        '</html>'
