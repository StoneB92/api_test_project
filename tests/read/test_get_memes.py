def test_list_of_all_memes(all_meme_endpoint):
    all_meme_endpoint.all_meme()
    all_meme_endpoint.check_response_status_code_is_correct()


