def test_delete_meme(delete_meme_endpoint, adding_meme):
    delete_meme_endpoint.delete_meme(adding_meme)
    delete_meme_endpoint.check_response_status_code_is_correct()
