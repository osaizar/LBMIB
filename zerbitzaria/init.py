# coding: latin-1
from database import Base, db_session, engine
from werkzeug.security import generate_password_hash
from sqlalchemy_utils import database_exists, create_database, drop_database
from models import Device, User, Session, Message, Permission
import os
import sys
import pwd

def add(data):
    db_session.add(data)
    db_session.commit()

def check_root():
    if os.geteuid() != 0:
        return False
    else:
        return True

def check_user(username):
    try:
        pwd.getpwnam(username)
        return True
    except:
        return False

def main():
    """
    if not check_root():
        print ("[!] Exekutatu scipt hau root moduan")
        sys.exit(1)
    """

    if database_exists(engine.url):
        ans = raw_input("[+] lbmib datu basea aurkitu da, ezabatzea nahi? (b/e) ")
        if ans.lower() == "b":
            ans = raw_input("[!] Seguru zaude? (b/e) ")
            if ans.lower() == "b":
                print ("[+] Datu basea ezabatzen...")
                drop_database(engine.url)
                print ("[+] Datu basea sortzen...")
                create_database(engine.url)
                Base.metadata.create_all(engine)
    else:
        ans = raw_input("[+] lbmib datu basea ez da aurkitu, sortzea nahi? (b/e) ")
        if ans.lower() == "b":
                print ("[+] Datu basea sortzen...")
                create_database(engine.url)
                Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()
