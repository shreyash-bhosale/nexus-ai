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

    @staticmethod
    def grayscale(image: LoadedImage) -> LoadedImage:
        logger.info("Converting image to grayscale...")
        return ImageProcessor.to_grayscale(image)

    @staticmethod
    def denoise(image: LoadedImage) -> LoadedImage:
        logger.info("Removing image noise...")
        return ImageProcessor.denoise(image)

    @staticmethod
    def enhance_contrast(image: LoadedImage) -> LoadedImage:
        logger.info("Enhancing image contrast...")
        return ImageProcessor.enhance_contrast(image)

    @staticmethod
    def save(image: LoadedImage, output_path: Path) -> None:
        logger.info("Saving processed image: {}", output_path)
        ImageProcessor.save_image(image, output_path)