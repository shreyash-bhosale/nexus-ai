"""
Screen Capture Service

Captures the user's primary monitor and saves the screenshot.
"""

from datetime import datetime

import mss
from PIL import Image

from nexus_ai.core.logger import logger
from nexus_ai.core.paths import SCREENSHOTS_DIR
from nexus_ai.features.capture.exceptions import ScreenCaptureError
from nexus_ai.features.capture.models import CaptureResult


class ScreenCaptureService:
    """Service responsible for capturing the user's screen."""

    def capture_screen(self) -> CaptureResult:
        """
        Capture the primary monitor.

        Returns:
            CaptureResult

        Raises:
            ScreenCaptureError
        """

        logger.info("Starting screen capture...")

        try:
            with mss.mss() as sct:
                monitor = sct.monitors[1]

                screenshot = sct.grab(monitor)

                image = Image.frombytes(
                    "RGB",
                    screenshot.size,
                    screenshot.rgb,
                )

                timestamp = datetime.now()

                filename = timestamp.strftime("%Y-%m-%d_%H-%M-%S.png")

                output_path = SCREENSHOTS_DIR / filename

                image.save(output_path)

                logger.info(f"Screenshot saved: {output_path}")

                return CaptureResult(
                    image_path=output_path,
                    captured_at=timestamp,
                    width=image.width,
                    height=image.height,
                )

        except Exception as exc:
            logger.exception("Screen capture failed.")
            raise ScreenCaptureError(str(exc)) from exc