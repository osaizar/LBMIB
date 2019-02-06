from models import User
from database import db_session

import sys

def add(data):
    try:
        db_session.add(data)
        db_session.commit()
        return True, data
    except Exception as e:
        db_session.flush()
        return False, e


def main():
    if len(sys.argv) < 2:
        print("[-] Argumentuak ahaztu zaizkizu")
    elif sys.argv[1] == "new-user":
        if len(sys.argv) != 4:
            print("[-] new-user <username> <password>")
        else:
            user = User(sys.argv[2], sys.argv[3])
            correct, data = add(user)
            if correct:
                print("[+] "+data.username+" gehitu da")
            else:
                print("[!] Errorea! "+str(data))

if __name__ == '__main__':
    main()
