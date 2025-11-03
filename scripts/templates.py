### Main repository README templates ###

MAIN_README_TEMPLATE = """# leetcode-solutions
Collection of my solutions to various leetcode problems.

<!--TODO (maybe):  add statistics section with # of problems solved, which difficulty, etc.-->

## Scripts
- `add_solution-py`: automatically adds directories + files and invokes `generate_readme()`. Use flag "--help" for script usage.
- `generate_readme.py`: generates new main README.md file with updated *Contents* table.

## Contents
| # | Problem Title | Language(s) | Link |
|:-:|---------------|-------------|------|"""

MAIN_README_TABLE_ENTRY = "\n| {number} | {title} | {languages} | [View](./problems/{dir_name}) |"



### Problem directory templates ###

SOURCE_FILE_HEADER = """{prefix} Problem:  {number}. {title}
{prefix} Link:  {url}
{prefix} Solution:  TODO: <approach> ~ <complexity>\n\n"""

PROBLEM_README_TEMPLATE = """# Problem: {number}. {title}

**Link:** [{url}]({url})

**Summary:** TODO: \<description>

**Solution Approach:**
- TODO: \<approach> ~ \<complexity> ~ \<language>"""
