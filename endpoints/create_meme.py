import requests
from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    def new_meme(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        return self.response

    def new_meme_without_authorize(self, body):
        headers = None
        self.response = requests.post(self.url, json=body, headers=headers)
        return self.response
