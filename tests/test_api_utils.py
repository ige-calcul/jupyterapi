from jupyterapi import api_utils


class TestApiUtils:
    def test_get_api_path_if_empty(self):
        assert api_utils._get_api_path("") == "/api/"

    def test_get_api_path_if_space(self):
        assert api_utils._get_api_path(" ") == "/api/"

    def test_get_api_path_if_slash(self):
        assert api_utils._get_api_path("/") == "/api/"

    def test_get_api_path_if_slashes(self):
        assert api_utils._get_api_path("///") == "/api/"

    def test_get_api_path_if_api(self):
        assert api_utils._get_api_path("api") == "/api/"

    def test_get_api_path_if_correct(self):
        assert api_utils._get_api_path("/api/") == "/api/"

    def test_get_api_path_if_short(self):
        assert api_utils._get_api_path("test") == "/test/api/"

    def test_get_api_path_if_long(self):
        assert api_utils._get_api_path("/test/test/api/") == "/test/test/api/"

    def test_get_api_path_if_api_first(self):
        assert api_utils._get_api_path("api/test") == "/api/test/api/"

    def test_get_api_path_if_not_stripped(self):
        assert api_utils._get_api_path("  test/api/  ") == "/test/api/"
