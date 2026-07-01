"""
OCR exceptions.
"""


class OCRException(Exception):
    """Base exception for OCR."""


class OCRInitializationError(OCRException):
    """Raised when the OCR engine cannot be initialized."""


class OCRProcessingError(OCRException):
    """Raised when OCR processing fails."""