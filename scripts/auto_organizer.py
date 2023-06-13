import os
import re
from datetime import datetime


def get_job_date(job_line):
    """
    Extracts the date from a job line in the table.
    Returns a datetime object representing the date.
    """
    date_match = re.search(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b", job_line)
    if date_match:
        date_str = f"{date_match.group(1)}/{date_match.group(2)}/{date_match.group(3)}"
        return datetime.strptime(date_str, "%m/%d/%Y").date()
    return None


def sort_jobs(jobs):
    """
    Sorts the jobs list by date in descending order.
    Jobs with non-standard dates are placed after the valid dates.
    Invalid jobs without dates are sorted alphabetically.
    """
    valid_jobs = []
    invalid_jobs = []
    for job in jobs:
        job_date = get_job_date(job)
        if job_date:
            valid_jobs.append((job_date, job))
        else:
            invalid_jobs.append(job)

    sorted_valid_jobs = sorted(valid_jobs, key=lambda x: x[0], reverse=True)
    sorted_jobs = [job[1] for job in sorted_valid_jobs] + sorted(invalid_jobs)
    return sorted_jobs


def get_jobs_table_lines(lines):
    """
    Extracts the lines containing the jobs table from the README.
    Returns the start and end line indices of the table,
    and the lines in between as a list.
    """
    start, end = -1, -1
    for i, line in enumerate(lines):
        if "## Jobs" in line:
            start = i + 2
        if start != -1 and line.startswith("-END OF LIST-"):
            end = i
            break

    if start == -1 or end == -1:
        print("Could not find Jobs table in README.md")
        return None

    table_lines = lines[start + 4 : end - 1]
    return start, end, table_lines


def capitalize_jobs(table_lines):
    """
    Capitalizes the job names in the table lines.
    """
    return [
        re.sub(r"\[(.*?)\]\(", lambda m: f"[{m.group(1)[0].upper() + m.group(1)[1:]}](", line) for line in table_lines
    ]


def overwrite_table(lines, start, end, header_and_formatting, sorted_table_lines):
    """
    Overwrites the old jobs table with the new sorted and capitalized table lines.
    """
    lines[start : end - 1] = header_and_formatting + sorted_table_lines
    return lines


def organize_readme():
    filename = os.path.join(os.path.dirname(__file__), "..", "README.md")
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Extract the lines containing the jobs table
    table_start, table_end, table_lines = get_jobs_table_lines(lines)
    if table_lines is None:
        return

    # Header and table formatting
    header_and_formatting = lines[table_start : table_start + 4]

    # Sort and capitalize the jobs
    sorted_table_lines = sort_jobs(table_lines)
    sorted_table_lines = capitalize_jobs(sorted_table_lines)

    # Overwrite the old table with the new one
    lines = overwrite_table(lines, table_start, table_end, header_and_formatting, sorted_table_lines)

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)

    print("README.md was organized successfully!")


if __name__ == "__main__":
    organize_readme()
