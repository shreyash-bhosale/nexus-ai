"""
Image processing utilities.
"""

from pathlib import Path

import cv2

from nexus_ai.features.vision.exceptions import ImageLoadError
from nexus_ai.features.vision.models import LoadedImage


class ImageProcessor:
    """
    Provides image loading and preprocessing utilities.
    """

    @staticmethod
    def load_image(path: Path) -> LoadedImage:
        """
        Load an image from disk.
        """

        if not path.exists():
            raise ImageLoadError(f"Image does not exist: {path}")

        image = cv2.imread(str(path))

        if image is None:
            raise ImageLoadError(f"Failed to load image: {path}")

        height, width, channels = image.shape

        return LoadedImage(
            path=path,
            width=width,
            height=height,
            channels=channels,
            image=image,
        )