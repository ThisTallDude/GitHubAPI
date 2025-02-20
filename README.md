# GitHubAPI
Develop a testing framework using PyTest to interact with GitHub, including creating repositories, making changes through the GitHub UI, and verifying those changes. 

1. Setup the Project:
Use Python 3.x, PyTest, Selenium/Playwright, and Requests.
Define a conftest.py file for global test configurations, fixtures, and parallel execution.
Integrate environment configuration using pytest.ini or a .env file for secure storage of GitHub credentials (e.g., tokens).

2. API Test Cases:
Create Repository:
Use the GitHub API to create a new repository programmatically.
List and Validate Repository Details:
List all repositories for a user and validate if the newly created repository exists.
Branch and Commit Operations:
Create a new branch via the GitHub API.
Push a commit to the branch using the git.
Pull Request Validation:
Automate the creation of pull requests and verify the PR’s metadata (title, description, changes).
Delete Repository
Perform a DELETE request to remove the repository.

3. UI Test Cases:
Create Repository (UI):
Automate repository creation through GitHub’s UI.
Modify Files and Submit PR:
Open a repository.
Edit a file (e.g., README.md) via the GitHub UI and commit the changes.
Create and submit a pull request through the UI.
Review and Merge Pull Request:
Automate the review process:
Validate modified files.
Merge the PR.
Validate Pull Request Changes:
Verify file modifications in git.

4. Git Operations:
Clone Repository:
Use Git commands to clone the repository locally.
Validate the presence of the modified files and content.
Push Changes via Code:
Automate the following steps:
Create a branch locally.
Modify a file.
Commit and push the changes.
Use the GitHub UI to approve and merge the PR.

Reporting and Logging:
Execution:

All tests that can run in parallel, should run in parallel
Reporting:
Integrate Allure or HTML reporting to provide detailed test execution reports for both API and UI tests.
Logging:
Implement a logging mechanism (using Python’s logging library).

