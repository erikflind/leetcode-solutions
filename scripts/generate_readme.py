import os
from pathlib import Path
from tempfile import NamedTemporaryFile

# Local modules
from config import ROOT_DIR, PROBLEMS_DIR, SUPPORTED_LANGUAGES
from templates import MAIN_README_TEMPLATE, MAIN_README_TABLE_ENTRY


# Build language lookup (extension -> name)
EXT_TO_LANG = {ext: name for name, ext, _ in SUPPORTED_LANGUAGES.values()}


def generate_readme():
    # Write to temp file before overwriting old README to avoid partial writes
    temp_name = None    # initialize outside try block to avoid UnboundLocalError
    try:
        with NamedTemporaryFile("w", encoding="utf-8", dir=ROOT_DIR, delete=False) as temp:
            temp_name = temp.name

            temp.write(MAIN_README_TEMPLATE)

            # Write README contents table entries by checking the problems directory contents
            with os.scandir(PROBLEMS_DIR) as dirs:
                # Ensure that the problem sub-directories are sorted
                for d in sorted(dirs, key=lambda e: e.name):
                    # Skip non-dir entries
                    if not d.is_dir(): continue

                    parts = d.name.split("-")
                    number = parts[0]
                    title = " ".join(parts[1:]).title()
                    dir_name = d.name

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
                            match = EXT_TO_LANG.get(file_ext.lower())
                            if match: languages.add(match)

                    # Sort the languages for consistency
                    languages = sorted(languages)

                    temp.write(MAIN_README_TABLE_ENTRY.format(number=number, title=title, languages=", ".join(languages), dir_name=dir_name))

            temp.flush()    # write buffer to file
            os.fsync(temp.fileno())     # ensure file content on disk

        # replace original README (if it exists; otherwise simply renames temp file)
        os.replace(temp_name, ROOT_DIR / "README.md")

        # Ensure directory entry durability on POSIX systems
        if os.name == "posix":
            dir_fd = os.open(str(ROOT_DIR), os.O_DIRECTORY)
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
    
    except Exception:
        # Cleanup temp file if something failed before replace
        if temp_name:
            try: os.remove(temp_name)
            except FileNotFoundError: pass
        raise   # re-raise original exception after cleanup


if __name__ == "__main__":
    generate_readme()
