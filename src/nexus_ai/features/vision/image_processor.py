"""
Image processing utilities.
"""

from pathlib import Path

import cv2
import numpy as np

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

    @staticmethod
    def resize(image: LoadedImage, scale: float = 2.0) -> LoadedImage:
        """
        Resize image before OCR.
        """

        resized = cv2.resize(
            image.image,
            None,
            fx=scale,
            fy=scale,
            interpolation=cv2.INTER_CUBIC,
        )

        height, width = resized.shape[:2]

        channels = 1 if len(resized.shape) == 2 else resized.shape[2]

        return LoadedImage(
            path=image.path,
            width=width,
            height=height,
            channels=channels,
            image=resized,
        )

    @staticmethod
    def to_grayscale(image: LoadedImage) -> LoadedImage:
        """
        Convert an image to grayscale.
        """

        gray = cv2.cvtColor(image.image, cv2.COLOR_BGR2GRAY)

        return LoadedImage(
            path=image.path,
            width=image.width,
            height=image.height,
            channels=1,
            image=gray,
        )

    @staticmethod
    def denoise(image: LoadedImage) -> LoadedImage:
        """
        Remove noise from an image.
        """

        denoised = cv2.fastNlMeansDenoising(image.image)

        return LoadedImage(
            path=image.path,
            width=image.width,
            height=image.height,
            channels=1,
            image=denoised,
        )

    @staticmethod
    def enhance_contrast(image: LoadedImage) -> LoadedImage:
        """
        Enhance image contrast using histogram equalization.
        """

        enhanced = cv2.equalizeHist(image.image)

        return LoadedImage(
            path=image.path,
            width=image.width,
            height=image.height,
            channels=1,
            image=enhanced,
        )

    @staticmethod
    def adaptive_threshold(image: LoadedImage) -> LoadedImage:
        """
        Convert image into a binary image.
        """

        threshold = cv2.adaptiveThreshold(
            image.image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            11,
        )

        return LoadedImage(
            path=image.path,
            width=image.width,
            height=image.height,
            channels=1,
            image=threshold,
        )

    @staticmethod
    def sharpen(image: LoadedImage) -> LoadedImage:
        """
        Sharpen image.
        """

        kernel = np.array(
            [
                [0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0],
            ]
        )

        sharpened = cv2.filter2D(
            image.image,
            -1,
            kernel,
        )

        return LoadedImage(
            path=image.path,
            width=image.width,
            height=image.height,
            channels=1,
            image=sharpened,
        )

    @staticmethod
    def save_image(image: LoadedImage, output_path: Path) -> None:
        """
        Save an image to disk.
        """

        output_path.parent.mkdir(parents=True, exist_ok=True)

        success = cv2.imwrite(str(output_path), image.image)

        if not success:
            raise ImageLoadError(f"Failed to save image: {output_path}")