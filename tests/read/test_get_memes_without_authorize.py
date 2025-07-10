def test_list_of_all_memes(all_meme_endpoint):
    all_meme_endpoint.all_meme_without_authorize()
    all_meme_endpoint.status_code_in_case_without_authorize()


