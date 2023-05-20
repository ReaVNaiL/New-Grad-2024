import os
import re

def organize_readme():
    filename = os.path.join(os.path.dirname(__file__), "..", "README.md")
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # find the start and end of the Jobs table
    start, end = -1, -1
    for i, line in enumerate(lines):
        if "## Jobs" in line:
            start = i + 2
        if start != -1 and line.startswith("-END OF LIST-"):
            end = i
            break

    if start == -1 or end == -1:
        print("Could not find Jobs table in README.md")
        return

    # Header and table formatting
    header_and_formatting = lines[start:start + 4]

    # Actual data in table
    table_lines = lines[start + 4:end - 1]

    # Process lines containing '|', sort and capitalize
    table_lines_to_sort = sorted(table_lines, key=lambda x: x.split("|")[1].strip().lower())
    table_lines_to_sort = [re.sub(r'\[(.*?)\]\(', lambda m: f'[{m.group(1)[0].upper() + m.group(1)[1:]}](', line) for line in table_lines_to_sort]

    # overwrite the old table with the new one
    lines[start:end - 1] = header_and_formatting + table_lines_to_sort
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
        
    print("README.md updated")


if __name__ == "__main__":
    organize_readme()
