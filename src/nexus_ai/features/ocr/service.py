"""
OCR Service
"""

from pathlib import Path

from loguru import logger

from nexus_ai.features.ocr.engine import OCREngine
from nexus_ai.features.ocr.models import OCRResult


class OCRService:

    def __init__(self):

        logger.info("Loading PaddleOCR...")

        self.engine = OCREngine()

        logger.success("PaddleOCR Loaded.")

    def extract(self, image_path: Path) -> OCRResult:

        logger.info("Running OCR...")

        result = self.engine.extract_text(image_path)

        logger.success(
            "OCR Finished (Confidence {:.2f})",
            result.confidence,
        )

        return result