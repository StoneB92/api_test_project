import pytest
import requests


def test_list_of_all_memes(authorize):
    headers = {'Authorization': f'{authorize}'}
    response = requests.get('http://167.172.172.115:52355/meme', headers=headers)
    assert response.status_code == 200


def test_get_one_meme(authorize):
    headers = {'Authorization': f'{authorize}'}
    response = requests.get('http://167.172.172.115:52355/meme/1', headers=headers)
    print(response.text)
    assert response.status_code == 200


def test_adding_meme(authorize):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    headers = {'Authorization': f'{authorize}'}
    response = requests.post('http://167.172.172.115:52355/meme', json=body, headers=headers)
    print(response.text)
    assert response.status_code == 200


def test_meme_change(authorize, adding_meme):
    body = {
        "id": adding_meme,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    headers = {'Authorization': f'{authorize}'}
    response = requests.put(f'http://167.172.172.115:52355/meme/{adding_meme}', json=body, headers=headers)
    print(adding_meme)
    assert response.status_code == 200


def test_deleting_meme(authorize, adding_meme):
    headers = {'Authorization': f'{authorize}'}
    response = requests.delete(f'http://167.172.172.115:52355/meme/{adding_meme}', headers=headers)
    assert response.status_code == 200
