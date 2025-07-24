import pytest


@pytest.mark.parametrize('invalid_text', [45234, [11, 43], [{"test": 1, "test2": 2}]])
def test_update_meme_invalid_text(update_meme_endpoint, adding_meme_teardown, invalid_text):
    body = {
        "id": adding_meme_teardown,
        "text": invalid_text,
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.assert_status_code_is_400_on_error()


@pytest.mark.parametrize('invalid_url', [1, [1, 2], [{"test": 1, "test2": 2}]])
def test_update_meme_invalid_url(update_meme_endpoint, adding_meme_teardown, invalid_url):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": invalid_url,
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.assert_status_code_is_400_on_error()


@pytest.mark.parametrize('invalid_tags', [
    1,
    "test",
    [{"test": 1, "test2": 2}],
    None,
    {},
    [123],
    [None]
])
def test_update_meme_invalid_tags(update_meme_endpoint, adding_meme_teardown, invalid_tags):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": invalid_tags,
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.assert_status_code_is_400_on_error()


@pytest.mark.parametrize('invalid_info', [1, "1", [1, 2]])
def test_update_meme_invalid_info(update_meme_endpoint, adding_meme_teardown, invalid_info):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": invalid_info
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.assert_status_code_is_400_on_error()


def test_update_meme_without_body(update_meme_endpoint, adding_meme_teardown):
    body = {}
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.assert_status_code_is_400_on_error()
