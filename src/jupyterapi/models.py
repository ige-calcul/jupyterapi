"""Model classes return by HTTP request to Jupyter Server API."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Result:
    """Result returned from low-level RestAdapter after an HTTP request."""

    status_code: int
    message: str = ""
    data: list[dict] = field(default_factory=list)


@dataclass
class Content:
    """Result returned from "contents" endpoint."""

    name: str
    path: str
    type: str
    writable: bool
    created: str
    last_modified: str
    size: int
    mimetype: str
    content: str
    format: str
    hash: str
    hash_algorithm: str
