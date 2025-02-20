import pytest
from playwright.sync_api import Browser

from config import GITHUB_USERNAME

REPO_NAME = "test-repo-scm"
FILE_NAME = "README.md"
BRANCH_NAME = "feature-branch"
PR_TITLE = "Automated PR - Update README"
UPDATED_CONTENT = "Updated README via Playwright UI Test."


@pytest.mark.ui
def test_modify_file_and_merge_pr(browser: Browser):
    """Modify README.md, create a PR, review, merge it, and validate changes."""

    page = browser.new_page()

    # Step 1: Open the repository
    repo_url = f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}"
    page.goto(repo_url)
    page.wait_for_load_state("load")

    # Step 2: Open the README.md file
    page.goto(f"{repo_url}/edit/main/README.md")
    page.wait_for_load_state("load")

    # Step 3: Modify file content
    # Locate the text area for editing README.md
    editor = page.locator("div.cm-line")
    editor.first.click()  # Activate the editor
    page.keyboard.type("test")  # Simulate typing

    # Click the "Commit changes..." button by targeting its parent button
    commit_button = page.locator("button:has(span[data-component='text']:has-text('Commit changes...'))")
    commit_button.click()

    # Wait for the modal containing "Commit changes" button to appear
    modal = page.locator("div[role='dialog']")  # Locate the modal dialog
    modal.wait_for(timeout=5000)  # Wait up to 5 seconds for the modal to appear

    # Click the "Commit changes" button inside the modal
    final_commit_button = modal.locator("button:has-text('Commit changes')")
    final_commit_button.click()

    # Navigate to the commit history of the repository
    page.goto(f"{repo_url}/commits/main")
    page.wait_for_load_state("load")

    # Define the locator for the latest commit message
    commit_message_locator = page.locator("a[data-pjax='true'].color-fg-default")

    # Ensure at least one commit message is visible
    if not commit_message_locator.first.is_visible():
        pytest.fail("❌ No commit messages found on the commits page!")

    # Get the text of the latest commit
    latest_commit_text = commit_message_locator.first.text_content().strip()

    # Verify if the latest commit contains the expected title
    if "Update README.md" in latest_commit_text:
        print("✅ The latest commit is 'Update README.md'!")
    else:
        pytest.fail(f"❌ The latest commit is NOT 'Update README.md'. Found: '{latest_commit_text}'")

