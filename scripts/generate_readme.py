import os
from pathlib import Path


MAIN_README_TEMPLATE = """# leetcode-solutions
Collection of my solutions to various leetcode problems.

<!--TODO (maybe):  add statistics section with # of problems solved, which difficulty, etc.-->

## Scripts
- `add_solution-py`: automatically adds directories + files and invokes `generate_readme()`. Use flag "--help" for script usage.
- `generate_readme.py`: generates new main README.md file with updated *Contents* table.

## Contents
| # | Problem Title | Language(s) | Link |
|:-:|---------------|-------------|------|"""

README_ENTRY = "\n| {number} | {title} | {languages} | [View](./problems/{dir_name}) |"

SUPPORTED_LANGUAGES = {"java":   ("Java",   ".java",  "//"),
                       "c":      ("C",      ".c",     "//"),
                       "python": ("Python", ".py",    "#")}

# Build language lookup (extension -> name)
EXT_TO_LANG = {ext: name for name, ext, _ in SUPPORTED_LANGUAGES.values()}


PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "problems"


def generate_readme():
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(MAIN_README_TEMPLATE)

        # Add all of the contents table entries
        with os.scandir(PROBLEMS_DIR) as entries:
            # Ensure that the problem sub-directories are sorted
            for entry in sorted(entries, key=lambda e: e.name):
                # Skip non-dir entries
                if not entry.is_dir(): continue

                temp = entry.name.split("-")
                number = temp[0]
                title = " ".join(temp[1:]).title()
                dir_name = entry.name

                dir_path = PROBLEMS_DIR / dir_name
                
                # Prevent duplicates if there are more than one source file per a given language
                languages = set()
                
                # Locate files within sub-directory; check file extensions
                with os.scandir(dir_path) as files:
                    for file in files:
                        # Skip non-file entries
                        if not file.is_file(): continue

                        # Add language names to set based on the file extensions found
                        _, file_ext = os.path.splitext(file.name)
                        match = EXT_TO_LANG.get(file_ext)
                        if match: languages.add(match)

                # Sort the languages for consistency
                languages = sorted(languages)

                # Write new entry to README contents table
                f.write(README_ENTRY.format(number=number, title=title, languages=", ".join(languages), dir_name=dir_name))


if __name__ == "__main__":
    generate_readme()
