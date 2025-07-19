def test_get_token(authorize_endpoint):
    token = authorize_endpoint.fetch_new_token()
    authorize_endpoint.check_response_status_code_is_correct()
    assert token is not None
