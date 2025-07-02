import requests
import os

TOKEN_FILE = 'token.txt'


class Authorize:

    def __init__(self, authorize):
        self.response = None
        self.authorize = authorize

    def check_response_status_code_is_correct(self):
        print(self.response.status_code)
        print(self.response.text)
        assert self.response.status_code == 200

    @staticmethod
    def read_token_from_file():
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, 'r') as f:
                return f.read().strip()
        return None

    @staticmethod
    def write_token_to_file(token):
        with open(TOKEN_FILE, 'w') as f:
            f.write(token)

    def check_token_validity(self, token):
        self.response = requests.get(f'http://167.172.172.115:52355/authorize/{token}')
        if self.response.status_code == 200:
            if 'Token is alive' in self.response.text:
                return True
            else:
                return False
        else:
            return False

    def fetch_new_token(self):
        body = {"name": "PeterB92"}
        self.response = requests.post('http://167.172.172.115:52355/authorize', json=body)
        data = self.response.json()
        token = list(data.values())[0]
        return token
