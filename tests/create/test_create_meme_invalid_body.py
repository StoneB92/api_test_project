def test_adding_meme_body_text_int(create_meme_endpoint):
    body = {
        "text": 111,
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_body_text_array(create_meme_endpoint):
    body = {
        "text": [11, 43],
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_body_text_object(create_meme_endpoint):
    body = {
        "text": {"test": 1, "test2": 2},
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_body_url_int(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": 1,
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_body_url_array(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": [1, 2],
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_body_url_object(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": {"test": 1, "test2": 2},
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_body_tags_int(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": 1,
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_body_tags_string(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": "test",
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_body_tags_object(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": {"test": 1, "test2": 2},
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_body_info_int(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": 1
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_body_info_string(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": "1"
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_body_info_array(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": [1, 2]
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()


def test_adding_meme_without_body(create_meme_endpoint):
    body = {}
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.status_code_in_case_of_error()

