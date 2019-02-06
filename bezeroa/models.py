import json

class Token():
    def __init__(self, auth, code = False):
        self.auth = auth
        self.code = code

    def toJSON(self):
        return json.dumps({"auth" : self.auth})
