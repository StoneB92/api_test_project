import requests
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    def delete_meme(self, adding_meme, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/{adding_meme}', headers=headers)
        return self.response

    def delete_meme_without_authorize(self, adding_meme):
        headers = None
        self.response = requests.delete(f'{self.url}/{adding_meme}', headers=headers)
        return self.response
