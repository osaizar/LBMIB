from flask import Flask, request, render_template, abort, jsonify, after_this_request
from werkzeug.security import generate_password_hash, check_password_hash
import random, string
import os

import db_helper as db
from validator import validate_json, validate_schema, validate_token
from logger import Logger
from models import Device, User, Session, Message, Permission

PORT = 5000
ADDR = "0.0.0.0"

app = Flask(__name__)
logger = Logger().get_logger()

# Help functions
def token_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Main App route:
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")


@app.route('/ajax/add_device', methods=["POST"])
@validate_json
@validate_token
def add_device():
    try:
        token = request.headers["token"] # TODO: Wrapper bat?
        user = db.get_user_by_token(token)
        if user == None:
            return jsonify({"error" : "Gakoa ez da zuzena"}), 200

        data = request.get_json(silent = True) # device auth
        device = db.get_device_by_code(data["code"])

        if device == None :
            return jsonify({"error" : "Kodea ez da baliozkoa"}), 400
        if db.device_has_owner(device.id):
            return jsonify({"error" : "Kodea ez da baliozkoa"}), 400

        if db.add(Permission(user.id, device.id, Permission.OWNER)) == False:
            return jsonify({"error" : "Errorea datubasean"}), 500

        logger.info("Device bati jabea jarri zaio. Auth:"+device.auth+" UserId:"+str(user.id)+" addr:"+str(request.remote_addr))

        return jsonify({"success" : "true"}), 200
    except Exception, e:
        logger.error("Errorea 'add_device' : "+str(e)+" "+str(request.remote_addr))
        abort(500)

# Device functions
@app.route('/device/state', methods=["POST"])
@validate_json
def device_state():
    try:
        data = request.get_json(silent = True) # device auth, message date
        device = db.get_device_by_auth(data["auth"])

        if device != None:
            return jsonify({"error" : "Auth-kodea ez da baliozkoa"}), 400

        if not db.device_has_owner(device.id):
            return jsonify({"state" : "no-owner"}), 200
        elif:
            pass # TODO: Mezu berririk badago, bidali

        return jsonify({"state" : "correct"}), 200
    except Exception, e:
        logger.error("Errorea 'device_state' : "+str(e)+" "+str(request.remote_addr))
        abort(500)


@app.route('/device/new', methods=["POST"])
@validate_json
def device_new():
    try:
        data = request.get_json(silent = True) # device auth
        if db.get_device_by_auth(data["auth"]) != None:
            return jsonify({"error" : "Auth-kodea ez da baliozkoa"}), 400

        device = db.add(Device(data["auth"], Device.generate_code()))

        if device == False:
            return jsonify({"error" : "Errorea datubasean"}), 500

        logger.info("Device berri bat sortu da. Auth:"+device.auth+" Code:"+device.code+" addr:"+str(request.remote_addr))

        return jsonify({"success" : "true", "code" : device.code}), 200
    except Exception, e:
        logger.error("Errorea 'device_new' : "+str(e)+" "+str(request.remote_addr))
        abort(500)

if __name__ == '__main__':
   app.run(host=ADDR, port=PORT)
