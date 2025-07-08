def test_adding_meme(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme(body)
    create_meme_endpoint.check_response_status_code_is_correct()
