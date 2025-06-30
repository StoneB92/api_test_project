class Endpoint:
    def __init__(self, authorize):
        self.url = 'http://167.172.172.115:52355/meme'
        self.response = None
        self.headers = {'Authorization': f'{authorize}'}

    def check_response_status_code_is_correct(self):
        print(self.response.status_code)
        print(self.response.text)
        assert self.response.status_code == 200
