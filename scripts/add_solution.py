import os
import sys
import argparse
from pathlib import Path
from urllib.parse import urlparse

from generate_readme import generate_readme
from config import PROBLEMS_DIR, SUPPORTED_LANGUAGES, PAD_WIDTH
from templates import SOURCE_FILE_HEADER, PROBLEM_README_TEMPLATE


def wrapped_generate_readme():
    try:
        generate_readme()
    except Exception:
        print("Warning! Something went wrong during main README generation.")
        print("Please verify integrity of README file and/or rerun script with '--regen' flag to regenerate README.")
        raise

def confirm(prompt: str) -> bool:
    while True:
        answer = input(prompt + " [y/n] ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please input either 'y' or 'n'.")


# Names of the supported languages
SUPPORTED_NAMES = {name for name, _, _ in SUPPORTED_LANGUAGES.values()}

# PARSE AND HANDLE ARGUMENTS
parser = argparse.ArgumentParser(
    description="Purpose: Auto-generates directories & template files and updates main README when adding new leetcode solution.",
    epilog=f"Supported languages: {', '.join(sorted(SUPPORTED_NAMES))}")

# Add command line arguments
parser.add_argument("number", type=int, nargs="?", help="leetcode problem number")
parser.add_argument("url", nargs="?", help="URL link to leetcode problem")
parser.add_argument("--language", "--l", nargs="*", 
                    help="list of programming language names of source files to add (case insensitive)")
parser.add_argument("--regen", action="store_true", help="regenerate main README and exit")

# Parse arguments
args = parser.parse_args()

# Short circuit for --regen flag
if args.regen:
    wrapped_generate_readme()
    print("Main README successfully regenerated.")
    sys.exit(0)

# Validate non-optional arguments
missing = []
if args.number is None:
    missing.append("'number'")
if args.url is None:
    missing.append("'url'")
if missing:
    parser.error(f"Missing arguments! {', '.join(missing)} required unless --regen flag is provided.")

number: int = args.number
padded = f"{number:0{PAD_WIDTH}d}"
url:str = args.url.strip()
languages: list[str] = [lang.strip().lower() for lang in args.language or []]

# Supported languages error handling
unsupported = [lang for lang in languages if lang not in {name.lower() for name in SUPPORTED_NAMES}]
if unsupported:
    quoted_output = [f"'{lang}'" for lang in unsupported]
    print(f"Unsupported language(s): {', '.join(quoted_output)}")
    print(f"Please try one of: {', '.join(sorted(SUPPORTED_NAMES))}")
    sys.exit(1)


# EXTRACT RELEVANT INFO FROM URL
# Normalize URL; ensure consistent scheme
if not url.startswith(("http://", "https://")):
    url = "https://" + url

# Extract parts of url path; drop the empty segments
parsed_url = urlparse(url)
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

# Target directory
target_dir = PROBLEMS_DIR / f"{padded}-{slug}"

append = False  # whether the user wants to append files to existing target_dir

# Exact directory already exists; prompt user to confirm before proceeding
if target_dir.is_dir():
    if confirm(f"Problem folder '{padded}-{slug}' already exists. Add additional source files?"):
        append = True
    else:
        sys.exit(0)

# Check for number collisions with different slugs
if not append:
    collisions = [d for d in PROBLEMS_DIR.glob(f"{padded}-*") if d.is_dir()]
    if collisions:
        existing = collisions[0].name
        print("WARNING: Number mismatch/typo!")
        print(f"> Existing: {existing}")
        print(f"> Requested: {padded}-{slug}")
        sys.exit(1)


# CREATE DIRECTORIES & FILES
target_dir.mkdir(parents=True, exist_ok=True)

source_file_name = slug.replace("-", "_")

# Create problem README
try:
    with open(target_dir / "README.md", "x", encoding="utf-8") as f:
        f.write(PROBLEM_README_TEMPLATE.format(number=number, title=title, url=url))
except FileExistsError:
    print(f"Warning: README already exists at '{target_dir}', skipping...")

# Create new program file(s) with the appropriate extension(s)
# Prompts a warning if the file already exist
for lang in languages:
    lang_name, extension, comment_style = SUPPORTED_LANGUAGES.get(lang)
    try:
        # Write source file with formatted header 
        with open(target_dir / (source_file_name + extension), "x", encoding="utf-8") as f:
            f.write(SOURCE_FILE_HEADER.format(prefix=comment_style, number=number, title=title, url=url))
    except FileExistsError:
        print(f"Warning: '{lang_name}' source file already exists at '{target_dir}', skipping...")


# Regenerate main README file
wrapped_generate_readme()
