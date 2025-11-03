import os
#from pathlib import Path
from config import PROBLEMS_DIR, SUPPORTED_LANGUAGES
from templates import MAIN_README_TEMPLATE, MAIN_README_TABLE_ENTRY


# Build language lookup (extension -> name)
EXT_TO_LANG = {ext: name for name, ext, _ in SUPPORTED_LANGUAGES.values()}


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
                f.write(MAIN_README_TABLE_ENTRY.format(number=number, title=title, languages=", ".join(languages), dir_name=dir_name))


if __name__ == "__main__":
    generate_readme()
