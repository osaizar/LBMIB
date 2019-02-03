from database import db_session
from sqlalchemy import and_, or_, func
# from models import

def add(data):
    try:
        db_session.add(data)
        db_session.commit()
        return int(data.id)
    except:
        db_session.flush()
        return False