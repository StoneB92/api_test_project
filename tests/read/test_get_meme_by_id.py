def test_get_one_meme(one_meme_endpoint, adding_meme_teardown):
    one_meme_endpoint.one_meme(adding_meme_teardown)
    one_meme_endpoint.check_response_status_code_is_correct()


def test_update_nonexistent_meme(all_meme_endpoint, one_meme_endpoint):
    nonexistent_mem_id = one_meme_endpoint.get_nonexistent_mem_id(all_meme_endpoint)
    one_meme_endpoint.one_meme(nonexistent_mem_id)
    one_meme_endpoint.assert_status_code_is_404_on_error()
