"""API helpers module."""

import urllib.parse

from .exceptions import JupyterApiError


def get_api_url(url: str) -> str:
    """Validate the Jupyter Server URL and return the main API endpoint."""
    # TODO(ekwaly): #0 raise Exception ?
    url_items = urllib.parse.urlparse(url)
    if not url_items.scheme or not url_items.netloc:
        # TODO(ekwaly): #0 put msg in logs
        msg = "URL without scheme or incomplete"
        raise JupyterApiError(msg)

    return urllib.parse.urlunparse(
        url_items._replace(
            path=_get_api_path(url_items.path),
            params="",
            query="",
            fragment="",
        ),
    )


def _get_api_path(url_path: str) -> str:
    """Format an url Jupyter Server path to retrieve the main API endpoint."""
    path_items = url_path.strip(" ").strip("/").split("/")
    if path_items[-1] != "api":
        path_items.append("api")

    if not path_items[0]:
        path_items.pop(0)

    return f"/{'/'.join(path_items)}/"
