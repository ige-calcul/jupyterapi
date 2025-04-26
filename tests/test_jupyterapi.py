from jupyterapi.rest_adapter import RestAdapter


class TestRestAdapter:
    def test_initialization(self):
        assert isinstance(RestAdapter("https://null", "token"), RestAdapter)
