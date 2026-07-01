"""
OCR engine implementation.
"""

from pathlib import Path

import easyocr

from nexus_ai.features.ocr.exceptions import (
    OCRInitializationError,
    OCRProcessingError,
)
from nexus_ai.features.ocr.models import OCRResult


class OCREngine:
    """
    Wrapper around the EasyOCR engine.
    """

    def __init__(self, languages: list[str] | None = None) -> None:
        """
        Initialize the OCR engine.

        Args:
            languages: List of language codes.

        Raises:
            OCRInitializationError
        """

        if languages is None:
            languages = ["en"]

        try:
            self._reader = easyocr.Reader(languages)
        except Exception as exc:
            raise OCRInitializationError(str(exc)) from exc

    def extract_text(self, image_path: Path) -> OCRResult:
        """
        Extract text from an image.

        Args:
            image_path: Path to the image.

        Returns:
            OCRResult

        Raises:
            OCRProcessingError
        """

        try:
            results = self._reader.readtext(str(image_path))

            if not results:
                return OCRResult(
                    image_path=image_path,
                    text="",
                    confidence=0.0,
                )

            text = " ".join(item[1] for item in results)

            confidence = (
                sum(item[2] for item in results)
                / len(results)
            )

            return OCRResult(
                image_path=image_path,
                text=text,
                confidence=confidence,
            )

        except Exception as exc:
            raise OCRProcessingError(str(exc)) from exc