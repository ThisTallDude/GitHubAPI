import pytest
import time
from playwright.sync_api import Browser
from tests.api.test_delete_repo import test_delete_repository

from config import GITHUB_USERNAME

REPO_NAME = "test-repo-scm"


@pytest.mark.ui
def test_create_repository_ui(browser: Browser):
    """Use saved session to create a repository without logging in."""

    # Step 1: Delete repository via API before creating it
    print(f"🔄 Deleting existing repository '{REPO_NAME}' before test...")
    test_delete_repository()

    page = browser.new_page()
    page.goto("https://github.com/")
    page.wait_for_load_state("load")

    # Debug: Print current page URL
    print(f"🔍 Current URL: {page.url}")

    # Navigate to repository creation page
    page.goto("https://github.com/new")
    page.wait_for_load_state("load")
    time.sleep(3)

    # Debug: Print current page URL
    print(f"🔍 Navigated to: {page.url}")

    # Fill in the repository name
    page.fill("input[aria-describedby='RepoNameInput-is-available RepoNameInput-message']", REPO_NAME)
    time.sleep(1)

    # Click the "Create repository" button
    create_button = page.locator("button:has-text('Create repository')")

    if create_button.is_visible():
        create_button.click()
        time.sleep(5)  # Wait for redirection to the repository page
    else:
        pytest.fail("❌ 'Create repository' button not found!")
