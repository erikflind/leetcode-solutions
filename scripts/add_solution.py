import os
import argparse
from pathlib import Path #TODO: refactor path handling using pathlib
from urllib.parse import urlparse
from generate_readme import generate_readme, SUPPORTED_LANGUAGES

# String templates / Constant variables
FILE_HEADER = "{0} Problem: {1}\n{0} Solution: TODO: <approach> ~ <complexity>\n\n"

PROBLEM_README_TEMPLATE = """# Problem: {0}

**Link:** [{1}]({1})

**Summary:** TODO: \<description>

**Solution Approach:**
- TODO: \<approach> ~ \<complexity> ~ \<language>"""

PROBLEMS_ROOT = "./problems"

# PARSE AND HANDLE ARGUMENTS
parser = argparse.ArgumentParser(
    description="Auto-generates directories & files and updates main README when adding new leetcode solution")

# Add command line arguments
parser.add_argument("number", type=int, help="leetcode problem number")
parser.add_argument("url", help="URL to ")
parser.add_argument( "--languages", "--l", nargs="*", help="language source files to add - case insensitive")

# Parse arguments
args = parser.parse_args()
number: int = args.number
url:str = args.url.strip()
languages: list[str] = [lang.strip().lower() for lang in args.languages or []]

# Pre-compute supported language names before loop
supported_lang_names = {name.lower() for name, _, _ in SUPPORTED_LANGUAGES}

# Supported languages error handling
for lang in languages:
    if lang not in supported_lang_names:
        print(f"Error! '{lang}' is currently not supported. Please try one of the supported languages:")
        for supp_lang in SUPPORTED_LANGUAGES: print(f" >> {supp_lang[0]}")
        exit(1)


# EXTRACT RELEVANT INFO FROM URL
parsed_url = urlparse(url)

# Extract parts of url path; drop the empty segments
path_parts = [p for p in parsed_url.path.split("/") if p]

# Strip url paths that are too long, for example:
#   https://leetcode.com/problems/add-two-numbers/submissions/1814956175/
#   --> https://leetcode.com/problems/add-two-numbers/ 
try:
    # The problem slug is immediately after "problems" in the url path
    i = path_parts.index("problems")
    slug = path_parts[i + 1]
except (ValueError, IndexError) as e:
    raise ValueError("URL provided does not contain /problems/<slug>/") from e

# Ensure url is in a short (canonical) format
url = f"{parsed_url.scheme}://{parsed_url.netloc}/problems/{slug}"

# Derive title from slug
title = slug.replace("-", " ").title()


# CREATE DIRECTORIES & FILES
folder_name: str = f"{number:04d}-{slug}"
path: str = os.path.join(PROBLEMS_ROOT, folder_name)
file_name = slug.replace("-", "_")

os.makedirs(path, exist_ok=True)

# Create problem README
try:
    with open(f"{path}/README.md", "x") as f:
        f.write(PROBLEM_README_TEMPLATE.format(title, url))
except FileExistsError:
    print(f"README already exists at {path}, skipping...")

# Create new program files with the appropriate extension
# Throws an error if they already exist
for lang in languages:
    # SUPPORTED_LANGUAGES is a list of tuples with (lang_name, lang_file_ext, lang_comment_style)
    for supp_lang in SUPPORTED_LANGUAGES:
        if lang == supp_lang[0].lower():
            # Unpack tuple to retrieve language: name, extension and single-line comment style
            lang_name, lang_extension, lang_comment = supp_lang

            try:
                # Write source file with formatted header 
                with open(f"{path}/{file_name}{lang_extension}", "x") as f:
                    f.write(FILE_HEADER.format(lang_comment, url))
            except FileExistsError:
                print(f"'{lang_name}' source file already exists at {path}, skipping...")


# Regenerate main README file
generate_readme()
