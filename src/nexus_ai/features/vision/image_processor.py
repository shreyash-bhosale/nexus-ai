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

        Args:
            path: Path to the image.

        Returns:
            LoadedImage

        Raises:
            ImageLoadError: If the image cannot be loaded.
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
    def to_grayscale(image: LoadedImage) -> LoadedImage:
        """
        Convert an image to grayscale.

        Args:
            image: Loaded image.

        Returns:
            LoadedImage
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

        Args:
            image: Loaded image.

        Returns:
            LoadedImage
        """

        if image.channels == 1:
            denoised = cv2.fastNlMeansDenoising(image.image)
            channels = 1
        else:
            denoised = cv2.fastNlMeansDenoisingColored(image.image)
            channels = image.channels

        return LoadedImage(
            path=image.path,
            width=image.width,
            height=image.height,
            channels=channels,
            image=denoised,
        )

    @staticmethod
    def enhance_contrast(image: LoadedImage) -> LoadedImage:
        """
        Enhance image contrast using histogram equalization.

        Args:
            image: Loaded image.

        Returns:
            LoadedImage
        """

        if image.channels == 1:
            enhanced = cv2.equalizeHist(image.image)
            channels = 1
        else:
            lab = cv2.cvtColor(image.image, cv2.COLOR_BGR2LAB)
            l, a, b = cv2.split(lab)

            l = cv2.equalizeHist(l)

            lab = cv2.merge((l, a, b))
            enhanced = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
            channels = 3

        return LoadedImage(
            path=image.path,
            width=image.width,
            height=image.height,
            channels=channels,
            image=enhanced,
        )

    @staticmethod
    def save_image(image: LoadedImage, output_path: Path) -> None:
        """
        Save an image to disk.

        Args:
            image: Loaded image.
            output_path: Destination file path.

        Raises:
            ImageLoadError: If saving fails.
        """

        output_path.parent.mkdir(parents=True, exist_ok=True)

        success = cv2.imwrite(str(output_path), image.image)

        if not success:
            raise ImageLoadError(f"Failed to save image: {output_path}")