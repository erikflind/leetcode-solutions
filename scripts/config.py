from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

PROBLEMS_DIR = ROOT_DIR / "problems"

SUPPORTED_LANGUAGES = {
    "java":   ("Java",   ".java",  "//"),
    "c":      ("C",      ".c",     "//"),
    "python": ("Python", ".py",    "#")
}

# Used to pad "problem number" strings with 0's
PAD_WIDTH = 4  # related to number of existing leetcode problems (4-digit as of writing)
