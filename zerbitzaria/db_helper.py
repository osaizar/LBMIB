from database import db_session
from sqlalchemy import and_, or_, func
from models import Device, User, Session, Message, Permission

def add(data):
    try:
        db_session.add(data)
        db_session.commit()
        return data
    except:
        db_session.flush()
        return False

# User and Session

def get_user_by_id(userId):
    try:
        return User.query.filter(User.id == userId).one()
    except:
        return None

def get_user_by_username(username):
    try:
        return User.query.filter(User.username == username).first()
    except:
        return None

def get_user_by_token(token):
    try:
        session = get_session_by_token(token)
        return get_user_by_id(session.user)
    except:
        return None

def get_session_by_token(token):
    try:
        return Session.query.filter(Session.token == token).one()
    except:
        return None

def get_all_users():
    try:
        return User.query.all()
    except:
        return None

def delete_session_by_user(userId):
    try:
        Session.query.filter(Session.user == userId).delete()
        db_session.commit()
        return True
    except:
        return None

def change_user_password(userId, password):
    try:
        user = User.query.filter(User.id == userId).one()
        user.password = password
        db_session.commit()
        return True
    except:
        db_session.flush()
        return False

def delete_user_by_id(userId):
    try:
        user = User.query.filter(User.id == userId).one()
        delete_session_by_user(user.id)
        db_session.delete(user)
        db_session.commit()
        return True
    except:
        db_session.flush()
        return False

# Device
def get_device_by_id(deviceId):
    try:
        return Device.query.filter(Device.id == deviceId).one()
    except:
        return None

def get_device_by_code(deviceCode):
    try:
        return Device.query.filter(Device.code == deviceCode).one()
    except:
        return None

def get_device_by_auth(deviceAuth):
    try:
        return Device.query.filter(Device.auth == deviceAuth).one()
    except:
        return None

def device_has_owner(deviceId):
    try:
        owner = Permission.query.filter(and_(Permission.device == deviceId, Permission.level == Permission.OWNER)).one()
        return bool(owner == None) # TODO: Jaberik ez badago None?
    except:
        return None

# message

def get_messages_by_user(userId):
    try:
        return Message.query.filter(Message.author == userId).all()
    except:
        return None

def get_messages_to_device(deviceId):
    try:
        return Message.query.filter(Message.device == deviceId).all()
    except:
        return None
