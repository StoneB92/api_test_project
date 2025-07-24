def test_delete_nonexistent_meme(all_meme_endpoint, one_meme_endpoint, delete_meme_endpoint):
    nonexistent_mem_id = one_meme_endpoint.get_nonexistent_mem_id(all_meme_endpoint)
    delete_meme_endpoint.delete_meme(nonexistent_mem_id)
    delete_meme_endpoint.assert_status_code_is_404_on_error()
