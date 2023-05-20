## How to Contribute to 2024 New Grad Full-time Positions🎓💼

Thank you for your interest in contributing to the 2024 New Grad Full-time Positions repository! We appreciate your help in maintaining and expanding the table of job openings for new grads in various tech roles.

I'll do my best to keep them sorted **[A-Z]** by **company name**. If you see any mistakes or outdated information, please submit a pull request to update them. 

### Need Before You Contribute
* **Company Name**
* **Location**
* **Roles** / **Links** to Job Posting

### Adding A Job Opening / Updating A Job Opening

1. **Fork the Repository**: Click the "Fork" button at the top-right corner of the repository to create your own copy of the repository.
<br>

2. **Clone the Forked Repository**: Clone the forked repository to your local machine using the following command:
<br>

3. **Add the Job Opening**: Add the job opening to the table in the `README.md` file. 
Please follow the existing format of the table.

<details>
<summary><b>Table Example</b> -- click here</summary> <br>

- If you were **ADDING** a job opening for *Walmart*:

| Company Name        | Location       | Roles                | 
| --------------------| -------------- |--------------------- | 
| [Walmart](https://careers.walmart.com/) | Bentonville, AR (s) | [New Grad Software Engineer II](https://careers.walmart.com/)|


Placeholders for the table are as follows:
  - `Company Name`: The name of the company.
  - `Location`: The location(s) of the job opening.
  - `Roles`: Any additional Roles or links to the job posting.

```java
| [Company Name](link-to-job-posting) | Location (s)  | [Position Name](link-to-job-posting)|
```

<br>

- If **UPDATING** a job opening, please follow the same format as above, but replace the link to the job posting with the new link, or add a new position name separated by a comma.

| Company Name        | Location       | Roles                | 
| --------------------| -------------- |--------------------- | 
| [Walmart](https://careers.walmart.com/) | Bentonville, AR (s) | [New Grad Software Engineer II](https://careers.walmart.com/), [New Grad Product Manager](https://careers.walmart.com/)|

```java
| [Company Name](link-to-job-posting) | Location (s)  | [Position Name](link-to-job-posting), [New Position Name 2](link-to-job-posting-2)|
```


</details> 
<br>

5. **Commit the Changes**: Commit the changes to your forked repository using the following commands:

    ```bash
    git add .
    git commit -m "Add <Company Name> to the list"
    ```

6. **Create a Pull Request**:
    * You can create a pull request from your forked repository to the original repository by clicking on the **"Compare & pull request"** button on your forked repository page.

    **OR**

    * You can also create a pull request from your forked repository to the original repository using the following commands:

    ```bash
    git push origin main
    ```
    Then, create a pull request from your forked repository to the original repository. Please ensure that the pull request and commit message adhere to the [contribution guidelines](#guidelines).

    <br>

7. **Review Pending / Done!** 🎉 Thank you for your contribution! Your pull request will be reviewed and merged as soon as possible.

> ⚠️ NOTE: No worries, worst case scenario, we can always edit your pull request and fix any issues together.

### Removing A Job Opening

This section is for removing a job opening from the table in the `README.md` file.

It's very similar, assuming you have already forked the repository and cloned it to your local machine.

1. **Find the Job Opening**: Find the job opening you want to remove from the table in the `README.md` file.

2. **Close the Job Opening**: 
    - Simply add a 🔒 **[No Longer Available]** 🔒 or 🔒 **[Closed]** 🔒 before the Roles or links to the job posting.
    - Then remove the link to the job posting from both the company name and position name. *The parentheses should be empty*

<details>
<summary><b>Table Example</b></summary><br>

- This is what the *table* would look like if you were removing a job opening for *Walmart*:

| Company Name        | Location       | Roles                |
| --------------------| -------------- |--------------------- |
| [Walmart]() | Bentonville, AR (s) | 🔒 **[Closed]** 🔒 [New Grad Software Engineer II]()|

Placeholders for the table are as follows:
  - `Company Name`: The name of the company.
  - `Location`: The location(s) of the job opening.
  - `Roles`: Any additional Roles or links to the job posting.

```java
| [Company Name]() | Location (s)  | 🔒 **[Closed]** 🔒 [Position Name]()|
```

</details>

### Guidelines

- Please ensure that the job listings you add are for New Grad positions in the fields of:
    * **Software Engineering (SWE)** / **Software Development Engineer (SDE)**
    * **Quant Roles**
    * **Product Management (PM)** / **Product Manager (PM)**
    * **Other tech roles.**
- Make sure that the job openings are for the year 2024 and are located in the **United States**, **Remote**, or **Canada**.
- Provide accurate and up-to-date information for each job listing.
- Follow the existing format of the table in the `README.md` file.
- Not already listed in the table or previously submitted in a pull request.


### Thank You

We appreciate your contributions to the 2024 New Grad Full-time Positions repository! Your efforts help keep this resource valuable and up-to-date for new grads seeking job opportunities.

Good luck with your job search, and thank you for being a part of our community! 🌟