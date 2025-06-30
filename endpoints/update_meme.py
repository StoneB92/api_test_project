import requests
from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):

    def update_meme(self, adding_meme, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{adding_meme}', json=body, headers=headers)
        return self.response
