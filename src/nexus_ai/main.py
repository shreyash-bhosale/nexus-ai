from nexus_ai.core.logger import logger
from nexus_ai.core.settings import APP_NAME, VERSION
from nexus_ai.features.capture import ScreenCaptureService


def main() -> None:
    logger.info("=" * 60)
    logger.info(f"Starting {APP_NAME}")
    logger.info(f"Version: {VERSION}")

    capture_service = ScreenCaptureService()

    result = capture_service.capture_screen()

    logger.info(f"Resolution: {result.width} x {result.height}")
    logger.info(f"Saved to: {result.image_path}")

    logger.info("=" * 60)


if __name__ == "__main__":
    main()