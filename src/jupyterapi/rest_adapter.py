"""Adapter Design Pattern for Jupyter Server REST API."""

from __future__ import annotations

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

    def _do(
        self,
        http_method: str,
        endpoint: str,
        ep_params: dict | None = None,
        data: dict | None = None,
    ) -> list[dict]:
        """Run HTTP generic request to Jupyter Server API."""
        full_url = self.url + endpoint
        headers = {"Authorization": f"token {self._token}"}
        try:
            response = requests.request(
                http_method,
                url=full_url,
                verify=self._ssl_verify,
                headers=headers,
                params=ep_params,
                json=data,
                timeout=10,
            )
        except requests.exceptions.RequestException as e:
            msg = "Request failed"
            raise JupyterApiError(msg) from e
        data_out = response.json()
        if response.ok:
            return data_out

        raise JupyterApiError(data_out["message"])

    def get(self, endpoint: str, ep_params: dict | None = None) -> list[dict]:
        """Run HTTP GET request to Jupyter Server API."""
        return self._do(http_method="GET", endpoint=endpoint, ep_params=ep_params)

    def patch(
        self,
        endpoint: str,
        ep_params: dict | None = None,
        data: dict | None = None,
    ) -> None:
        """Run HTTP PATCH request to Jupyter Server API."""
        return self._do(
            http_method="PATCH",
            endpoint=endpoint,
            ep_params=ep_params,
            data=data,
        )

    def post(
        self,
        endpoint: str,
        ep_params: dict | None = None,
        data: dict | None = None,
    ) -> None:
        """Run HTTP POST request to Jupyter Server API."""
        return self._do(
            http_method="POST",
            endpoint=endpoint,
            ep_params=ep_params,
            data=data,
        )

    def put(
        self,
        endpoint: str,
        ep_params: dict | None = None,
        data: dict | None = None,
    ) -> None:
        """Run HTTP PUT request to Jupyter Server API."""
        return self._do(
            http_method="PUT",
            endpoint=endpoint,
            ep_params=ep_params,
            data=data,
        )

    def delete(
        self,
        endpoint: str,
        ep_params: dict | None = None,
        data: dict | None = None,
    ) -> None:
        """Run HTTP DELETE request to Jupyter Server API."""
        return self._do(
            http_method="DELETE",
            endpoint=endpoint,
            ep_params=ep_params,
            data=data,
        )
