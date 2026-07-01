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

    logger.info("=" * 70)
    logger.info("🚀 Starting NEXUS AI")
    logger.info("Version : 0.1.0")
    logger.info("=" * 70)

    # ----------------------------------------------------------
    # Capture Screenshot
    # ----------------------------------------------------------

    capture_service = ScreenCaptureService()
    capture = capture_service.capture_screen()

    logger.success("Screenshot captured successfully.")
    logger.info("Path       : {}", capture.image_path)
    logger.info("Resolution : {} x {}", capture.width, capture.height)

    # ----------------------------------------------------------
    # Load Image
    # ----------------------------------------------------------

    image = VisionService.load(capture.image_path)

    logger.success("Image loaded.")
    logger.info("Resolution : {} x {}", image.width, image.height)

    # ----------------------------------------------------------
    # Resize
    # ----------------------------------------------------------

    resized = VisionService.resize(image)

    resized_path = PROCESSED_DIR / "resized.png"

    VisionService.save(resized, resized_path)

    logger.success("Saved resized image.")

    # ----------------------------------------------------------
    # Grayscale
    # ----------------------------------------------------------

    grayscale = VisionService.grayscale(resized)

    grayscale_path = PROCESSED_DIR / "grayscale.png"

    VisionService.save(grayscale, grayscale_path)

    logger.success("Saved grayscale image.")

    # ----------------------------------------------------------
    # Denoise
    # ----------------------------------------------------------

    denoised = VisionService.denoise(grayscale)

    denoised_path = PROCESSED_DIR / "denoised.png"

    VisionService.save(denoised, denoised_path)

    logger.success("Saved denoised image.")

    # ----------------------------------------------------------
    # Contrast Enhancement
    # ----------------------------------------------------------

    enhanced = VisionService.enhance_contrast(denoised)

    enhanced_path = PROCESSED_DIR / "enhanced.png"

    VisionService.save(enhanced, enhanced_path)

    logger.success("Saved enhanced image.")

    logger.info("=" * 70)
    logger.info("Vision preprocessing completed.")
    logger.info("=" * 70)

    # ----------------------------------------------------------
    # OCR
    # ----------------------------------------------------------

    ocr_service = OCRService()

    result = ocr_service.extract(enhanced_path)

    logger.info("")
    logger.info("=" * 70)
    logger.info("📄 OCR RESULT")
    logger.info("=" * 70)

    logger.info("Confidence : {:.2f}", result.confidence)
    logger.info("Lines      : {}", result.line_count)
    logger.info("Words      : {}", result.word_count)

    logger.info("-" * 70)

    if result.text:

        print()
        print("=" * 70)
        print("EXTRACTED TEXT")
        print("=" * 70)
        print()
        print(result.text)
        print()
        print("=" * 70)

    else:

        logger.warning("No text detected.")

    logger.info("")
    logger.info("=" * 70)
    logger.success("NEXUS AI Finished Successfully.")
    logger.info("=" * 70)


if __name__ == "__main__":
    main()