import requests
from endpoints.endpoint import Endpoint


class GetOneMeme(Endpoint):
    def one_meme(self, adding_meme, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/{adding_meme}', headers=headers)
        return self.response

    def one_meme_without_authorize(self, adding_meme):
        headers = None
        self.response = requests.get(f'{self.url}/{adding_meme}', headers=headers)
        return self.response
