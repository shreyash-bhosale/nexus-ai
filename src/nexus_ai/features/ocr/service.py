"""
OCR service.
"""

from nexus_ai.features.ocr.engine import OCREngine


class OCRService:
    """
    Coordinates OCR operations.
    """

    def __init__(self) -> None:
        self.engine = OCREngine()