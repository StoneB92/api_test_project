import pytest


def test_endpoint_adding_meme(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.check_response_status_code_is_correct()


@pytest.mark.parametrize('body_text', ['calm down', ' ', '', '!@#$%^&*()', '!@#test'])
def test_adding_meme_with_another_body(create_meme_endpoint, delete_meme_endpoint, body_text):
    body = {
        "text": body_text,
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    response = create_meme_endpoint.new_meme(body)
    create_meme = response.json()
    object_id = response.json()['id']
    assert create_meme['text'] == body['text']
    assert create_meme['url'] == body['url']
    assert create_meme['tags'] == body['tags']
    assert create_meme['info']['color'] == body['info']['color']
    delete_response = delete_meme_endpoint.delete_meme(object_id)
    print(delete_response.text)
    assert delete_response.status_code == 200


@pytest.mark.parametrize('body_url',
                         ['https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg',
                          ' ',
                          '',
                          '!@#$%^&*()',
                          '!@#test'
                          ]
                         )
def test_adding_meme_with_another_url(create_meme_endpoint, delete_meme_endpoint, body_url):
    body = {
        "text": "calm down",
        "url": body_url,
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    response = create_meme_endpoint.new_meme(body)
    create_meme = response.json()
    object_id = response.json()['id']
    assert create_meme['text'] == body['text']
    assert create_meme['url'] == body['url']
    assert create_meme['tags'] == body['tags']
    assert create_meme['info']['color'] == body['info']['color']
    delete_response = delete_meme_endpoint.delete_meme(object_id)
    print(delete_response.text)
    assert delete_response.status_code == 200


@pytest.mark.parametrize('body_tags', [
    ['lemur'],
    [' '],
    [''],
    ['!@#$%^&*()'],
    ['!@#test']
])
def test_adding_meme_with_another_tags(create_meme_endpoint, delete_meme_endpoint, body_tags):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": body_tags,
        "info": {"color": ['red', "white"]}
    }
    response = create_meme_endpoint.new_meme(body)
    create_meme = response.json()
    object_id = response.json()['id']
    assert create_meme['text'] == body['text']
    assert create_meme['url'] == body['url']
    assert create_meme['tags'] == body['tags']
    assert create_meme['info']['color'] == body['info']['color']
    delete_response = delete_meme_endpoint.delete_meme(object_id)
    print(delete_response.text)
    assert delete_response.status_code == 200


@pytest.mark.parametrize('body_info', [
    {"color": ['red', "white"]},
    {"color": [' ', "123"]},
    {"color": ['', "$#@$!"]},
    {"color": ['2312test', "___"]}
])
def test_adding_meme_with_another_info(create_meme_endpoint, delete_meme_endpoint, body_info):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": body_info
    }
    response = create_meme_endpoint.new_meme(body)
    create_meme = response.json()
    object_id = response.json()['id']
    assert create_meme['text'] == body['text']
    assert create_meme['url'] == body['url']
    assert create_meme['tags'] == body['tags']
    assert create_meme['info']['color'] == body_info['color']
    delete_response = delete_meme_endpoint.delete_meme(object_id)
    print(delete_response.text)
    assert delete_response.status_code == 200
