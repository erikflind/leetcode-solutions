from pathlib import Path

PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "problems"

SUPPORTED_LANGUAGES = {"java":   ("Java",   ".java",  "//"),
                       "c":      ("C",      ".c",     "//"),
                       "python": ("Python", ".py",    "#")}
