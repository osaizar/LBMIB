from flask import Flask, request, render_template, abort, jsonify, after_this_request
from werkzeug.security import generate_password_hash, check_password_hash
import random, string
import os

import db_helper as db
from validator import validate_json, validate_schema, validate_token
from logger import Logger
# from models import *

PORT = 5000
ADDR = "0.0.0.0"

app = Flask(__name__)
logger = Logger().get_logger()

# Imports
@app.route("/img/logo.png")
def logoPNG():
    return app.send_static_file("img/logo.png")

@app.route("/img/logo_osoa.png")
def logoOsoaPNG():
    return app.send_static_file("img/logo_osoa.png")

@app.route("/img/paper.png")
def paperPNG():
    return app.send_static_file("img/paper.png")

@app.route("/css/client.css")
def clientCSS():
    return app.send_static_file("css/client.css")

@app.route("/css/react-table.css")
def reacttableCSS():
    return app.send_static_file("css/react-table.css")

@app.route("/css/react-select.css")
def reactselectCSS():
    return app.send_static_file("css/react-select.css")

@app.route("/lib/bootstrap/css/bootstrap.css")
def bootstrapCSS():
    return app.send_static_file("bower_components/bootstrap/dist/css/bootstrap.css")

@app.route("/js/client.js")
def clientJS():
    return app.send_static_file("js/client.js")

@app.route("/js/sorttable.js")
def sorttableJS():
    return app.send_static_file("js/sorttable.js")

@app.route("/lib/jquery/jquery.js")
def jqueryJS():
    return app.send_static_file("bower_components/jquery/dist/jquery.js")

@app.route("/lib/bootstrap/js/bootstrap.js")
def bootstrapJS():
    return app.send_static_file("bower_components/bootstrap/dist/js/bootstrap.js")

@app.route("/lib/bootstrap/fonts/glyphicons-halflings-regular.ttf")
def bootstrapGlyphiconTTF():
    return app.send_static_file("bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.ttf")

@app.route("/lib/bootstrap/fonts/glyphicons-halflings-regular.woff")
def bootstrapGlyphiconWOFF():
    return app.send_static_file("bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.woff")

@app.route("/lib/bootstrap/fonts/glyphicons-halflings-regular.woff2")
def bootstrapGlyphiconWOFF2():
    return app.send_static_file("bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.woff2")

# Help functions
def token_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Main App route:
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

if __name__ == '__main__':
   app.run(host=ADDR, port=PORT)