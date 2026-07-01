"""
Data models for the vision module.
"""

from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass(slots=True)
class LoadedImage:
    """
    Represents an image loaded into memory.
    """

    path: Path
    width: int
    height: int
    channels: int
    image: np.ndarray