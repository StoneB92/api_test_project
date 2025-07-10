import requests
from endpoints.endpoint import Endpoint


class GetAllMeme(Endpoint):
    def all_meme(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(self.url, headers=headers)
        return self.response

    def all_meme_without_authorize(self):
        headers = None
        self.response = requests.get(self.url, headers=headers)
        return self.response
