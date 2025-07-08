import pytest
import requests
from endpoints.create_meme import CreateMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_one_meme import GetOneMeme
from endpoints.get_all_meme import GetAllMeme
from endpoints.authorize import Authorize


@pytest.fixture(scope='session')
def authorize(authorize_endpoint):
    token = authorize_endpoint.read_token_from_file()
    if token and authorize_endpoint.check_token_validity(token):
        return token
    else:
        new_token = authorize_endpoint.fetch_new_token()
        authorize_endpoint.write_token_to_file(new_token)
        return new_token


@pytest.fixture()
def adding_meme_teardown(authorize):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    headers = {'Authorization': f'{authorize}'}
    response = requests.post('http://167.172.172.115:52355/meme', json=body, headers=headers)
    object_id = response.json()['id']
    yield object_id
    delete_response = requests.delete(f'http://167.172.172.115:52355/meme/{object_id}', headers=headers)
    print(delete_response.text)
    assert delete_response.status_code == 200


@pytest.fixture()
def adding_meme(authorize):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    headers = {'Authorization': f'{authorize}'}
    response = requests.post('http://167.172.172.115:52355/meme', json=body, headers=headers)
    object_id = response.json()['id']
    return object_id


@pytest.fixture()
def create_meme_endpoint(authorize):
    return CreateMeme(authorize)


@pytest.fixture()
def update_meme_endpoint(authorize):
    return UpdateMeme(authorize)


@pytest.fixture()
def delete_meme_endpoint(authorize):
    return DeleteMeme(authorize)


@pytest.fixture()
def one_meme_endpoint(authorize):
    return GetOneMeme(authorize)


@pytest.fixture()
def all_meme_endpoint(authorize):
    return GetAllMeme(authorize)


@pytest.fixture(scope='session')
def authorize_endpoint():
    return Authorize(authorize)
