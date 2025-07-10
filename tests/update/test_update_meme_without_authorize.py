def test_update_meme(update_meme_endpoint, adding_meme_teardown):
    body = {
        "id": adding_meme_teardown,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme_without_authorize(adding_meme_teardown, body)
    update_meme_endpoint.status_code_in_case_without_authorize()
