"""Main interface to interact with Jupyter Server API."""

from __future__ import annotations

import urllib
from typing import TYPE_CHECKING

from .models import Content
from .rest_adapter import RestAdapter

if TYPE_CHECKING:
    import logging


class JupyterApi:
    def __init__(
        self,
        url: str,
        token: str,
        *,
        ssl_verify: bool = True,
        logger: logging.Logger | None = None,
    ):
        self._rest_adapter = RestAdapter(
            url,
            token,
            ssl_verify=ssl_verify,
            logger=logger,
        )

    def get_content(self, path: str = "") -> Content:
        path_escaped = urllib.parse.quote(path, safe="")
        result = self._rest_adapter.get(f"contents/{path_escaped}")
        return Content(**result.data)
