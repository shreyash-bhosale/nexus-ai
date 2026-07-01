from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class CaptureResult:
    """
    Represents a completed screen capture.
    """

    image_path: Path
    captured_at: datetime
    width: int
    height: int