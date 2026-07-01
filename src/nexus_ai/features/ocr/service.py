"""
OCR service.
"""

from pathlib import Path

from loguru import logger

from nexus_ai.features.ocr.engine import OCREngine
from nexus_ai.features.ocr.models import OCRResult


class OCRService:
    """
    Coordinates OCR operations.
    """

    def __init__(self) -> None:
        """
        Initialize the OCR service.
        """

        self.engine = OCREngine()

    def extract(self, image_path: Path) -> OCRResult:
        """
        Extract text from an image.

        Args:
            image_path: Image path.

        Returns:
            OCRResult
        """

        logger.info("Running OCR on {}", image_path)

        result = self.engine.extract_text(image_path)

        logger.info(
            "OCR complete (confidence {:.2f})",
            result.confidence,
        )

        return result