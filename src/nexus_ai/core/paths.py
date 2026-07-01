from pathlib import Path

# ----------------------------
# Project Root
# ----------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[3]

# ----------------------------
# Main Directories
# ----------------------------

SRC_DIR = PROJECT_ROOT / "src"

ASSETS_DIR = PROJECT_ROOT / "assets"

DATA_DIR = PROJECT_ROOT / "data"

LOGS_DIR = PROJECT_ROOT / "logs"

DOCS_DIR = PROJECT_ROOT / "docs"

# ----------------------------
# Runtime Directories
# ----------------------------

SCREENSHOTS_DIR = DATA_DIR / "screenshots"

CACHE_DIR = DATA_DIR / "cache"

MEMORY_DIR = DATA_DIR / "memory"

EXPORTS_DIR = DATA_DIR / "exports"

# ----------------------------
# Ensure directories exist
# ----------------------------

for directory in (
    DATA_DIR,
    SCREENSHOTS_DIR,
    CACHE_DIR,
    MEMORY_DIR,
    EXPORTS_DIR,
    LOGS_DIR,
):
    directory.mkdir(parents=True, exist_ok=True)