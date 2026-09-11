"""True multimodal document-agent contract for TANIA."""

from pathlib import Path
from typing import Union

from .models import DocumentContext


SUPPORTED = {".pdf", ".docx", ".pptx", ".xlsx", ".xls", ".csv", ".txt", ".md",
             ".png", ".jpg", ".jpeg", ".webp", ".svg"}


class MultimodalDocumentAgent:
    def inspect(self, path: Union[str, Path]) -> DocumentContext:
        p = Path(path)
        if p.suffix.lower() not in SUPPORTED:
            raise ValueError(f"Unsupported document type: {p.suffix}")
        return DocumentContext(path=str(p), kind=p.suffix.lower())

    def build_grounded_request(self, question: str, context: DocumentContext) -> dict:
        return {
            "question": question,
            "document": context.path,
            "grounding": context.grounding,
            "visuals": context.visuals,
        }
