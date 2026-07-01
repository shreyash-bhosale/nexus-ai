from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class OCRResult:

    image_path: Path

    text: str

    confidence: float

    line_count: int

    word_count: int