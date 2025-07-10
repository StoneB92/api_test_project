def test_get_one_meme_without_authorize(one_meme_endpoint, adding_meme_teardown):
    one_meme_endpoint.one_meme_without_authorize(adding_meme_teardown)
    one_meme_endpoint.status_code_in_case_without_authorize()
