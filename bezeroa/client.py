from logger import Logger
from models import Token
import requests, json, time, string, random, sys

URL = "http://localhost:5000"
logger = Logger().get_logger()

token = False

def load_token():
    global token
    print "[DEBUG] Loading token"
    try:
        with open('token.json') as f:
            data = json.load(f)

        token = Token(data["auth"])
        return True
    except:
        return False

def generate_token():
    global token
    auth = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(15))
    token = Token(auth)

    with open('token.json', 'w') as f:
        f.flush()
        f.write(token.toJSON())

def get_state():
    global token
    json_data = {"auth" : token.auth}
    headers = {"Content-Type": "application/json"}
    r = requests.post(URL+"/device/state", json=json_data, headers=headers)
    if r.status_code != 200:
        return False
    else:
        return r.json()

def send_greeting():
    global token
    json_data = {"auth" : token.auth}
    headers = {"Content-Type": "application/json"}
    r = requests.post(URL+"/device/new", json=json_data, headers=headers)
    return bool(r.status_code == 200) , r.json()

def greet():
    global token
    succ, data = send_greeting()
    if succ:
        token.code = data["code"]
    elif data["error"] == "auth not valid":
        token = False
    else:
        print "[DEBUG] Error in the new-device request, "+data["error"]

def handshake():
    global token
    if not token.code: # coderik ez badago, berriz hasi prozesua
        token = False
    else:
        print "Enter the code: "+str(token.code) # TODO: pantailan erakutsi beharko da kodea

        state = get_state()["state"]
        while state == "no-owner": # kodeari itxaron
            state = get_state()["state"]
            time.sleep(1)

def initialization(state):
    global token
    if state == "new-device":
        print "[DEBUG] The device is new, greeting the server"
        greet()
    elif state == "no-owner":
        print "[DEBUG] The device has no owners, handshake needed"
        handshake()

def main():
    global token
    print "[DEBUG] Starting Program"

    if not load_token():
        print "[DEBUG] Token not found, generating"
        generate_token()

    state = get_state()["state"]
    while state == "new-device" or state == "no-owner":
        initialization(state)
        if not token:
            generate_token()

        state = get_state()["state"]

    print "[DEBUG] Initialization successful"

    # print "[DEBUG] State == False, error in the resquest."

    while True:
        state = get_state()
        print str(state) # Debug
        time.sleep(1)

if __name__ == '__main__':
    main()
