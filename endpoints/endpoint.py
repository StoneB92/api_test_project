class Endpoint:
    def __init__(self, authorize):
        self.url = 'http://167.172.172.115:52355/meme'
        self.response = None
        self.headers = {'Authorization': f'{authorize}'}

    def check_response_status_code_is_correct(self):
        print(self.response.status_code)
        print(self.response.text)
        assert self.response.status_code == 200

    def assert_status_code_is_400_on_error(self):
        print(self.response.status_code)
        print(self.response.text)
        assert self.response.status_code == 400

    def status_code_in_case_without_authorize(self):
        print(self.response.status_code)
        print(self.response.text)
        assert self.response.status_code == 401

    def assert_status_code_is_404_on_error(self):
        print(self.response.status_code)
        print(self.response.text)
        assert self.response.status_code == 404

    def get_nonexistent_mem_id(self, all_meme_endpoint):
        response = all_meme_endpoint.all_meme()
        data = response.json()['data']
        max_id = max(int(item['id']) for item in data)
        return max_id + 1
