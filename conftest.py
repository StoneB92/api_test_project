import pytest
import requests
import os
from endpoints.create_meme import CreateMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_one_meme import GetOneMeme
from endpoints.get_all_meme import GetAllMeme


TOKEN_FILE = 'tests/token.txt'


def read_token_from_file():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            return f.read().strip()
    return None


def write_token_to_file(token):
    with open(TOKEN_FILE, 'w') as f:
        f.write(token)


def check_token_validity(token):
    response = requests.get(f'http://167.172.172.115:52355/authorize/{token}')
    if response.status_code == 200:
        if 'Token is alive' in response.text:
            return True
        else:
            return False
    else:
        return False


def fetch_new_token():
    body = {"name": 'PeterB92'}
    response = requests.post('http://167.172.172.115:52355/authorize', json=body)
    data = response.json()
    token = list(data.values())[0]
    return token


@pytest.fixture(scope='session')
def authorize():
    token = read_token_from_file()
    if token and check_token_validity(token):
        return token
    else:
        new_token = fetch_new_token()
        write_token_to_file(new_token)
        return new_token


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
