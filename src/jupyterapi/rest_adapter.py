"""Adapter Design Pattern for Jupyter Server REST API."""

import requests
import urllib3

from .api_utils import get_api_url
from .exceptions import JupyterApiError


class RestAdapter:
    """API wrapper class to run generic HTTP requests."""

    def __init__(self, url: str, token: str, *, ssl_verify: bool = True) -> None:
        """Initialize the main API endpoint and set authentication token."""
        self.url = get_api_url(url)
        self._token = token
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def get(self, endpoint: str) -> list[dict]:
        """Run HTTP GET request to Jupyter Server API."""
        full_url = self.url + endpoint
        headers = {"Authorization": f"token {self._token}"}
        response = requests.get(
            url=full_url,
            verify=self._ssl_verify,
            headers=headers,
            timeout=10,
        )
        data_out = response.json()
        if response.ok:
            return data_out

        raise JupyterApiError(data_out["message"])
