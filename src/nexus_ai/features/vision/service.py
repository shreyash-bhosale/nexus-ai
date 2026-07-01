"""
Vision service.
"""

from pathlib import Path

from loguru import logger

from nexus_ai.features.vision.image_processor import ImageProcessor
from nexus_ai.features.vision.models import LoadedImage


class VisionService:
    """
    Coordinates vision operations.
    """

    @staticmethod
    def load(path: Path) -> LoadedImage:
        logger.info("Loading image: {}", path)
        return ImageProcessor.load_image(path)