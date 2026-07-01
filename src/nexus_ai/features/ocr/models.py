"""
OCR data models.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class OCRResult:
    """
    Represents the result of OCR processing.
    """

    image_path: Path
    text: str
    confidence: float