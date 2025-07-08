def test_adding_meme_without_authorize(create_meme_endpoint):
    body = {
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white"]}
    }
    create_meme_endpoint.new_meme_without_authorize(body)
    create_meme_endpoint.status_code_in_case_without_authorize()
