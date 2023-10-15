import os
import re
from datetime import datetime


class README:
    def __init__(self, lines, start, end, header_and_formatting, sorted_table_lines):
        self.lines = lines
        self.start = start
        self.end = end
        self.header_and_formatting = header_and_formatting
        self.sorted_table_lines = sorted_table_lines

    def overwrite_table(self):
        self.lines[self.start : self.end - 1] = self.header_and_formatting + self.sorted_table_lines


class READMEOrganizer:
    def __init__(self, filename):
        self.filename = filename

    def get_job_date(self, job_line):
        """
        Extracts the date from a job line in the table.
        Returns a datetime object representing the date.
        """
        date_match = re.search(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b", job_line)
        if date_match:
            date_str = f"{date_match.group(1)}/{date_match.group(2)}/{date_match.group(3)}"
            return datetime.strptime(date_str, "%m/%d/%Y").date()
        return None

    def sort_jobs(self, jobs):
        """
        Sorts the jobs list by date in descending order.
        Jobs with non-standard dates are placed after the valid dates.
        Invalid jobs without dates are sorted alphabetically.
        """
        valid_jobs = []
        invalid_jobs = []
        for job in jobs:
            job_date = self.get_job_date(job)
            if job_date:
                valid_jobs.append((job_date, job))
            else:
                invalid_jobs.append(job)

        sorted_valid_jobs = sorted(valid_jobs, key=lambda x: x[0], reverse=True)
        sorted_jobs = [job[1] for job in sorted_valid_jobs] + sorted(invalid_jobs)
        return sorted_jobs

    def get_jobs_table_lines(self, lines):
        """
        Extracts the lines containing the jobs table from the README.
        Returns the start and end line indices of the table,
        and the lines in between as a list.
        """
        start, end = -1, -1
        for i, line in enumerate(lines):
            if "## Jobs" in line:
                start = i + 2
            if start != -1 and line.startswith("[⬆️ Back to Top](#jobs)"):
                end = i
                break

        if start == -1 or end == -1:
            print("Could not find Jobs table in README.md")
            return None

        table_lines = lines[start + 4 : end - 1]
        return start, end, table_lines

    def capitalize_jobs(self, table_lines):
        """
        Capitalizes the job names in the table lines.
        """
        return [
            re.sub(r"\[(.*?)\]\(", lambda m: f"[{m.group(1)[0].upper() + m.group(1)[1:]}](", line)
            for line in table_lines
        ]

    def organize_readme(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("README.md not found.")
            return
        except PermissionError:
            print("Permission denied to read README.md.")
            return

        table_start, table_end, table_lines = self.get_jobs_table_lines(lines)
        if table_lines is None:
            return

        header_and_formatting = lines[table_start : table_start + 4]

        sorted_table_lines = self.sort_jobs(table_lines)
        sorted_table_lines = self.capitalize_jobs(sorted_table_lines)

        readme = README(lines, table_start, table_end, header_and_formatting, sorted_table_lines)
        readme.overwrite_table()

        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.writelines(readme.lines)
        except PermissionError:
            print("Permission denied to write to README.md.")
            return

        print("README.md was organized successfully!")


if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), "..", "README.md")
    organizer = READMEOrganizer(filename)
    organizer.organize_readme()
