### Main repository README templates ###

MAIN_README_TEMPLATE = """# leetcode-solutions
Collection of my solutions to various leetcode problems.

<!--TODO (maybe):  add statistics section with # of problems solved, which difficulty, etc.-->

## Scripts
- `add_solution-py`: automatically adds directories + files and calls `generate_readme()`. Use flag "--help" for script usage.
- `generate_readme.py`: generates new main README.md file with updated *Contents* table.
- `config.py`: exports filepaths and supported languages dict.
- `templates.py`: exports string templates for READMEs and source file header.

## Contents
| # | Problem Title | Language(s) | Link |
|:-:|---------------|-------------|------|"""


MAIN_README_TABLE_ENTRY = "\n| {number} | {title} | {languages} | [View](./problems/{dir_name}) |"



### Problem directory templates ###

PROBLEM_README_TEMPLATE = """# Problem: {number}. {title}

**Link:** [{url}]({url})

**Summary:**  \<description> [TODO]

**Solution Approach:**
- \<approach> ~ \<complexity> ~ \<language> [TODO]"""


SOURCE_FILE_HEADER = """{prefix} Problem:  {number}. {title}
{prefix} Solution:  <approach> ~ <complexity> [TODO]
{prefix} Link:  {url}\n\n"""
