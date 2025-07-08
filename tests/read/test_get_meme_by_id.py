def test_get_one_meme(one_meme_endpoint, adding_meme_teardown):
    one_meme_endpoint.one_meme(adding_meme_teardown)
    one_meme_endpoint.check_response_status_code_is_correct()
