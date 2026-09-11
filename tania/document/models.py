from dataclasses import dataclass, field


@dataclass
class DocumentContext:
    path: str
    kind: str
    grounding: list[dict] = field(default_factory=list)
    visuals: list[dict] = field(default_factory=list)
