import pytest


@pytest.mark.parametrize('invalid_text', [
    111,
    [11, 43],
    [{"test": 1, "test2": 2}]
])
def test_adding_meme_body_invalid_text(create_meme_endpoint, invalid_text):
    body = {
        "text": invalid_text,
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.assert_status_code_is_400_on_error()


@pytest.mark.parametrize('invalid_url', [
    1,
    [1, 2],
    [{"test": 1, "test2": 2}]
])
def test_adding_meme_body_invalid_url(create_meme_endpoint, invalid_url):
    body = {
        "text": "calm down",
        "url": invalid_url,
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.assert_status_code_is_400_on_error()


@pytest.mark.parametrize('invalid_tags', [
    1,
    "test",
    [{"test": 1, "test2": 2}],
    None,
    {},
    [123],
    [None]
])
def test_adding_meme_body_invalid_tags(create_meme_endpoint, invalid_tags):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": invalid_tags,
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.assert_status_code_is_400_on_error()


@pytest.mark.parametrize('invalid_info', [
    1,
    "1",
    [1, 2]
])
def test_adding_meme_body_invalid_info(create_meme_endpoint, invalid_info):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": invalid_info
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.assert_status_code_is_400_on_error()


def test_adding_meme_without_body(create_meme_endpoint):
    body = {}
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.assert_status_code_is_400_on_error()
