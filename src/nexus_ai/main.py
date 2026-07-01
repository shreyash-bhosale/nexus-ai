"""
Main entry point for NEXUS AI.
"""

from nexus_ai.core.logger import logger
from nexus_ai.features.capture.service import ScreenCaptureService
from nexus_ai.features.vision.service import VisionService


def main() -> None:
    """Run the NEXUS AI application."""

    logger.info("=" * 60)
    logger.info("Starting NEXUS AI")
    logger.info("Version: 0.1.0")

    # Capture a fresh screenshot
    capture_service = ScreenCaptureService()
    capture = capture_service.capture_screen()

    logger.info("Screenshot captured successfully.")
    logger.info("Path: {}", capture.image_path)
    logger.info("Resolution: {} x {}", capture.width, capture.height)

    # Load the captured screenshot
    image = VisionService.load(capture.image_path)

    logger.info("Image loaded successfully.")
    logger.info("Image Resolution: {} x {}", image.width, image.height)
    logger.info("Channels: {}", image.channels)

    logger.info("NEXUS AI is ready.")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()