"""
OCR Engine using PaddleOCR
"""

from pathlib import Path

from paddleocr import PaddleOCR

from nexus_ai.features.ocr.models import OCRResult


class OCREngine:
    """
    PaddleOCR wrapper.
    """

    def __init__(self) -> None:

        self.reader = PaddleOCR(
            lang="en",
            use_textline_orientation=True,
        )

    def extract_text(self, image_path: Path) -> OCRResult:

        result = self.reader.predict(str(image_path))

        if not result:
            return OCRResult(
                image_path=image_path,
                text="",
                confidence=0.0,
                line_count=0,
                word_count=0,
            )

        lines = []
        confidences = []

        for page in result:

            # PaddleOCR v3 Page object
            if hasattr(page, "rec_texts"):

                texts = page.rec_texts
                scores = page.rec_scores
                boxes = page.rec_boxes

            # Fallback
            else:

                texts = page.get("rec_texts", [])
                scores = page.get("rec_scores", [])
                boxes = page.get("rec_boxes", [])

            combined = list(zip(boxes, texts, scores))

            combined.sort(
                key=lambda item: (
                    item[0][1],   # y
                    item[0][0],   # x
                )
            )

            for _, text, score in combined:

                text = text.strip()

                if len(text) < 2:
                    continue

                if score < 0.50:
                    continue

                lines.append(text)
                confidences.append(score)

        final_text = "\n".join(lines)

        confidence = (
            sum(confidences) / len(confidences)
            if confidences
            else 0.0
        )

        return OCRResult(
            image_path=image_path,
            text=final_text,
            confidence=confidence,
            line_count=len(lines),
            word_count=len(final_text.split()),
        )