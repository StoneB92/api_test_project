def test_get_token(authorize_endpoint):
    authorize_endpoint.fetch_new_token()
    authorize_endpoint.check_response_status_code_is_correct()
