from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

PROBLEMS_DIR = ROOT_DIR / "problems"

SUPPORTED_LANGUAGES = {"java":   ("Java",   ".java",  "//"),
                       "c":      ("C",      ".c",     "//"),
                       "python": ("Python", ".py",    "#")}
