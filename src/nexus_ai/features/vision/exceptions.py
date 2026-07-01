"""
Custom exceptions for the vision module.
"""


class VisionError(Exception):
    """Base exception for all vision-related errors."""


class ImageLoadError(VisionError):
    """Raised when an image cannot be loaded."""