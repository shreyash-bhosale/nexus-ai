"""
NEXUS AI Entry Point
"""

from nexus_ai.core.logger import logger
from nexus_ai.core.paths import PROCESSED_DIR
from nexus_ai.features.capture.service import ScreenCaptureService
from nexus_ai.features.ocr.service import OCRService
from nexus_ai.features.vision.service import VisionService


def main() -> None:
    """
    Main application entry point.
    """

    logger.info("=" * 60)
    logger.info("Starting NEXUS AI")
    logger.info("Version: 0.1.0")

    # ---------------------------------------------------------
    # Capture Screen
    # ---------------------------------------------------------

    capture_service = ScreenCaptureService()
    capture = capture_service.capture_screen()

    logger.info("Screenshot captured successfully.")
    logger.info("Path: {}", capture.image_path)
    logger.info("Resolution: {} x {}", capture.width, capture.height)

    # ---------------------------------------------------------
    # Load Image
    # ---------------------------------------------------------

    image = VisionService.load(capture.image_path)

    logger.info("Image loaded successfully.")
    logger.info("Image Resolution: {} x {}", image.width, image.height)
    logger.info("Channels: {}", image.channels)

    # ---------------------------------------------------------
    # Vision Pipeline
    # ---------------------------------------------------------

    grayscale = VisionService.grayscale(image)

    grayscale_path = PROCESSED_DIR / "grayscale.png"
    VisionService.save(grayscale, grayscale_path)

    logger.info("Grayscale image saved: {}", grayscale_path)

    denoised = VisionService.denoise(grayscale)

    denoised_path = PROCESSED_DIR / "denoised.png"
    VisionService.save(denoised, denoised_path)

    logger.info("Denoised image saved: {}", denoised_path)

    enhanced = VisionService.enhance_contrast(denoised)

    enhanced_path = PROCESSED_DIR / "enhanced.png"
    VisionService.save(enhanced, enhanced_path)

    logger.info("Enhanced image saved: {}", enhanced_path)

    logger.info("Vision preprocessing pipeline completed successfully.")

    # ---------------------------------------------------------
    # OCR Pipeline
    # ---------------------------------------------------------

    ocr_service = OCRService()

    ocr_result = ocr_service.extract(enhanced_path)

    logger.info("=" * 60)
    logger.info("OCR RESULTS")
    logger.info("=" * 60)
    logger.info("Confidence: {:.2f}", ocr_result.confidence)
    logger.info("Extracted Text:")
    logger.info(ocr_result.text)
    logger.info("=" * 60)

    # ---------------------------------------------------------
    # Finish
    # ---------------------------------------------------------

    logger.info("NEXUS AI is ready.")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()