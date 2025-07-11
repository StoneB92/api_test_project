def test_update_meme_text_int(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": 45234,
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_text_array(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": [11, 43],
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_text_object(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": {"test": 1, "test2": 2},
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_url_int(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": 1,
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_url_array(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": [1, 2],
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_url_object(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": {"test": 1, "test2": 2},
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_tags_int(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": 1,
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_tags_string(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": "test",
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_tags_object(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": {"test": 1, "test2": 2},
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_info_int(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": 1
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_info_string(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": "1"
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_info_array(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": [1, 2]
    }
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()


def test_update_meme_without_body(update_meme_endpoint, adding_meme_teardown):
    body = {}
    update_meme_endpoint.update_meme(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_of_error()

