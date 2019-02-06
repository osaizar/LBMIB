from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date, DateTime
import datetime, string, random
from database import Base

class Device(Base):
    __tablename__ = "device"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(5), nullable=False)
    auth = Column(String(15), nullable=False)

    def __init__(self, auth, code):
        self.auth = auth
        self.code = code

    @staticmethod
    def generate_auth(size=15, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def generate_code(size=5, chars=string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def serialize(self):
        return {"id" : self.id , "username" : self.username}

class Session(Base):
    __tablename__ = "session"
    user = Column(Integer, ForeignKey("user.id"), primary_key=True)
    token = Column(String(20), nullable=False)
    token_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, user, token):
        self.user = user
        self.token = token

    def check_token_expired(self):
        cur_time = datetime.datetime.utcnow()
        expire_date = self.token_date + datetime.timedelta(days=2) # tokenak 2 egun irauten ditu
        if cur_time > expire_date:
            return True
        else:
            return False

class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(Integer, ForeignKey("user.id"), nullable=False)
    device = Column(Integer, ForeignKey("device.id"), nullable=False)
    message = Column(String(250), nullable=False)
    message_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, message, author, device):
        self.device = device
        self.author = author
        self.message = message

    def check_message_expired(self):
        cur_time = datetime.datetime.utcnow()
        expire_date = self.message_date + datetime.timedelta(days=1) # mezuak egun 1 irauten du
        if cur_time > expire_date:
            return True
        else:
            return False

class Permission(Base):
    __tablename__ = "permission"
    id = Column(Integer, primary_key = True, autoincrement = True)
    user = Column(Integer, ForeignKey("user.id"), nullable=False)
    device = Column(Integer, ForeignKey("device.id"), nullable=False)
    level = Column(Integer, nullable=False)

    OWNER = 0
    WRITE = 1

    def __init__(self, user, device, level):
        self.user = user
        self.level = level
        self.device = device
