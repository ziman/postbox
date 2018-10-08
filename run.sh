#!/bin/sh

#FLASK_DEBUG=1
FLASK_APP=postbox.py exec flask run -h 0.0.0.0 -p 8071
