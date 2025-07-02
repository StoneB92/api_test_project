import pytest
import requests
from endpoints.create_meme import CreateMeme


def test_get_token(authorize_endpoint):
    authorize_endpoint.fetch_new_token()
    authorize_endpoint.check_response_status_code_is_correct()


def test_list_of_all_memes(all_meme_endpoint):
    all_meme_endpoint.all_meme()
    all_meme_endpoint.check_response_status_code_is_correct()


def test_get_one_meme(one_meme_endpoint, adding_meme):
    one_meme_endpoint.one_meme(adding_meme)
    one_meme_endpoint.check_response_status_code_is_correct()


def test_adding_meme(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.check_response_status_code_is_correct()


def test_meme_change(update_meme_endpoint, adding_meme):
    body = {
        "id": adding_meme,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme, body)
    update_meme_endpoint.check_response_status_code_is_correct()


def test_deleting_meme(delete_meme_endpoint, adding_meme):
    delete_meme_endpoint.delete_meme(adding_meme)
    delete_meme_endpoint.check_response_status_code_is_correct()
