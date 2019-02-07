from functools import wraps
from datetime import datetime
import db_helper as db
from logger import Logger
from flask import jsonify, request, abort

logger = Logger().get_logger()

def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            js = request.json
            if js == None:
                raise Exception
        except:
            logger.error("400 Errorea, json-a ez da egokia "+str(request.remote_addr))
            return jsonify({"error": "Eskaera ez da egokia"}), 400
        return f(*args, **kw)
    return wrapper

def validate_token(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            if "token" not in request.headers:
                logger.warning("400 Errorea, tokenik ez."+str(request.remote_addr))
                return jsonify({"error" : "Gakorik ez"}), 400

            token = request.headers["token"]
            user = db.get_user_by_token(token)
            if user == None:
                logger.warning("400 Errorea, tokena ez da egokia. "+str(request.remote_addr))
                return jsonify({"error" : "Gakoa ez da zuzena"}), 400

            session = db.get_session_by_token(token)

            if session.check_token_expired():
                logger.warning("400 Errorea,"+user.username+" erabiltzailearen tokena iraungita dago. "+str(request.remote_addr))
                return jsonify({"error" : "Gakoa ez da zuzena"}), 400

        except Exception as e:
            logger.error("Extepzioa 'validate_token': "+str(e)+" "+str(request.remote_addr))
            return jsonify({"error": "Eskaera ez da egokia"}), 400

        return f(*args, **kw)
    return wrapper

def validate_schema(name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                validate(request.json, name)
            except Exception as e:
                return jsonify({"error": e.message}), 400
            return f(*args, **kw)
        return wrapper
    return decorator

def validate(input, name):
    if name == False:
        pass
    else:
        Exception("Ez dago izen hori duen eskemarik")
