"""Gemini multimodal adapter boundary used by TANIA document intelligence."""

from __future__ import annotations

import base64
from pathlib import Path
from typing import Union


class GeminiMultimodal:
    def __init__(self, client=None, model: str = "gemini-flash-latest"):
        self.client = client
        self.model = model

    def image_part(self, path: Union[str, Path]) -> dict:
        data = Path(path).read_bytes()
        return {
            "mime_type": self._mime(Path(path)),
            "data_base64": base64.b64encode(data).decode("ascii"),
        }

    @staticmethod
    def _mime(path: Path) -> str:
        return {
            ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
            ".webp": "image/webp", ".svg": "image/svg+xml"
        }.get(path.suffix.lower(), "application/octet-stream")
