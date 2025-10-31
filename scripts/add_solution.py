import argparse
from pathlib import Path
from urllib.parse import urlparse
from generate_readme import generate_readme, SUPPORTED_LANGUAGES

# String templates / Constant variables
FILE_HEADER = "{0} Problem:  {1}. {2}\n{0} Link:  {3}\n{0} Solution:  TODO: <approach> ~ <complexity>\n\n"

PROBLEM_README_TEMPLATE = """# Problem: {0}. {1}

**Link:** [{2}]({2})

**Summary:** TODO: \<description>

**Solution Approach:**
- TODO: \<approach> ~ \<complexity> ~ \<language>"""

PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "problems"


# PARSE AND HANDLE ARGUMENTS
parser = argparse.ArgumentParser(
    description="Auto-generates directories & files and updates main README when adding new leetcode solution")
#TODO: add list of supported languages to --help output

# Add command line arguments
parser.add_argument("number", type=int, help="leetcode problem number")
parser.add_argument("url", help="URL link to leetcode problem")
parser.add_argument( "--languages", "--l", nargs="*", help="language source files to add - case insensitive")

# Parse arguments
args = parser.parse_args()
number: int = args.number
url:str = args.url.strip()
languages: list[str] = [lang.strip().lower() for lang in args.languages or []]

# Pre-compute supported language names before loop
supported_lang_names = {name for name, _, _ in SUPPORTED_LANGUAGES}

# Supported languages error handling
unsupported = [lang for lang in languages if lang not in {name.lower() for name in supported_lang_names}]
if unsupported:
    quoted_output = [f"'{lang}'" for lang in unsupported]
    print(f"Error! Unsupported languages: {', '.join(quoted_output)}")
    print(f"Please try one of: {', '.join(supported_lang_names)}")
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
        f.write(PROBLEM_README_TEMPLATE.format(number, title, url))
except FileExistsError:
    print(f"README already exists at {folder_path}, skipping...")

# Create new program files with the appropriate extension
# Throws an error if they already exist
for lang in languages:
    # SUPPORTED_LANGUAGES is a list of tuples with (lang_name, lang_file_ext, lang_comment_style)
    for supported_lang in SUPPORTED_LANGUAGES:
        if lang == supported_lang[0].lower():
            # Unpack tuple to retrieve language: name, extension and single-line comment style
            lang_name, lang_extension, lang_comment = supported_lang

            try:
                # Write source file with formatted header 
                with open(folder_path / (source_file_name + lang_extension), "x", encoding="utf-8") as f:
                    f.write(FILE_HEADER.format(lang_comment, number, title, url))
            except FileExistsError:
                print(f"'{lang_name}' source file already exists at {folder_path}, skipping...")


# Regenerate main README file
generate_readme()
