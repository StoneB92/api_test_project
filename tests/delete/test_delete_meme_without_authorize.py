def test_delete_meme_without_authorize(delete_meme_endpoint, adding_meme):
    delete_meme_endpoint.delete_meme_without_authorize(adding_meme)
    delete_meme_endpoint.status_code_in_case_without_authorize()
