def test_update_nonexistent_meme(all_meme_endpoint, update_meme_endpoint):
    nonexistent_mem_id = all_meme_endpoint.get_nonexistent_mem_id(all_meme_endpoint)
    body = {
        "id": nonexistent_mem_id,
        "text": "calm down",
        "url": "https://infoglaz.ru/wp-content/uploads/1387527274_001.jpg",
        "tags": ["lemur", "stop"],
        "info": {"color": ['red', "white", "black"]}
    }
    update_meme_endpoint.update_meme(None, body)
    update_meme_endpoint.assert_status_code_is_404_on_error()
