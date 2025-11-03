import os
import argparse
#from pathlib import Path
from urllib.parse import urlparse
from config import PROBLEMS_DIR, SUPPORTED_LANGUAGES
from templates import SOURCE_FILE_HEADER, PROBLEM_README_TEMPLATE
from generate_readme import generate_readme


def numbered_dir_exists(number: int):
    """
    Returns boolean for whether problem folder with the given number exists.
    """
    with os.scandir(PROBLEMS_DIR) as entries:
        for entry in entries:
            if not entry.is_dir(): continue

            dir_number = int(entry.name.split("-")[0])

            if number == dir_number: return True
            
    return False


# PARSE AND HANDLE ARGUMENTS
parser = argparse.ArgumentParser(
    description="Auto-generates directories & files and updates main README when adding new leetcode solution")
#TODO: add list of supported languages to --help output

# Add command line arguments
parser.add_argument("number", type=int, help="leetcode problem number")
parser.add_argument("url", help="URL link to leetcode problem")
parser.add_argument( "--language", "--l", nargs="*", help="programming language names of source files to add (case insensitive)")

# Parse arguments
args = parser.parse_args()
number: int = args.number
url:str = args.url.strip()
languages: list[str] = [lang.strip().lower() for lang in args.language or []]

# Check for number mismatch; problem folder already existing
if numbered_dir_exists(number):
    print("WARNING: Number mismatch/typo!")
    print(f"> Problem folder with the number '{number:04d}' already exists.")
    exit(1)

# FIXME: now it's not possible to add additional source file types to an existing folder:
# >> check slug to see if url and dir name match > prompt if want to add additional source file (y/n)

# Supported languages error handling
supported = {lang[0] for lang in SUPPORTED_LANGUAGES.values()}
unsupported = [lang for lang in languages if lang not in {name.lower() for name in supported}]
if unsupported:
    quoted_output = [f"'{lang}'" for lang in unsupported]
    print(f"Unsupported language(s): {', '.join(quoted_output)}")
    print(f"Please try one of: {', '.join(sorted(supported))}")
    exit(1)


# EXTRACT RELEVANT INFO FROM URL
# Normalize URL; ensure consistent scheme
if not url.startswith(("http://", "https://")):
    url = "https://" + url

parsed_url = urlparse(url)

# Extract parts of url path; drop the empty segments
path_parts = [p for p in parsed_url.path.split("/") if p]

# Strip url paths that are too long, for example:
#   https://leetcode.com/problems/add-two-numbers/submissions/1814956175/
#   --> https://leetcode.com/problems/add-two-numbers/ 
try:
    # The problem slug comes immediately after "problems" in the url path
    i = path_parts.index("problems")
    slug = path_parts[i + 1]
except (ValueError, IndexError) as e:
    raise ValueError("URL provided does not contain /problems/<slug>/") from e

# Ensure url is in a short (canonical) format
url = f"{parsed_url.scheme}://{parsed_url.netloc}/problems/{slug}/"

# Derive title from slug
title = slug.replace("-", " ").title()


# CREATE DIRECTORIES & FILES
folder_name = f"{number:04d}-{slug}"
folder_path = PROBLEMS_DIR / folder_name
source_file_name = slug.replace("-", "_")

folder_path.mkdir(parents=True, exist_ok=True)

# Create problem README
try:
    with open(folder_path / "README.md", "x", encoding="utf-8") as f:
        f.write(PROBLEM_README_TEMPLATE.format(number=number, title=title, url=url))
except FileExistsError:
    print(f"Warning: README already exists at '{folder_path}', skipping...")

# Create new program file(s) with the appropriate extension(s)
# Prompts a warning if the file already exist
for lang in languages:
    lang_name, extension, comment_style = SUPPORTED_LANGUAGES.get(lang)
    try:
        # Write source file with formatted header 
        with open(folder_path / (source_file_name + extension), "x", encoding="utf-8") as f:
            f.write(SOURCE_FILE_HEADER.format(prefix=comment_style, number=number, title=title, url=url))
    except FileExistsError:
        print(f"Warning: '{lang_name}' source file already exists at '{folder_path}', skipping...")


# Regenerate main README file
generate_readme()
