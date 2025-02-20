import sys
import os
import requests
import pytest

# Ensure the root directory is in sys.path for proper imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now import config variables
from config import GITHUB_API_BASE_URL, HEADERS, GITHUB_USERNAME, TEST_REPO_NAME


def test_delete_repository():

    """Check if a GitHub repository exists."""
    url = f"{GITHUB_API_BASE_URL}/repos/{GITHUB_USERNAME}/{TEST_REPO_NAME}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        print(f"✅ Repository '{TEST_REPO_NAME}' exists.")
        return True
    elif response.status_code == 404:
        print(f"⚠️ Repository '{TEST_REPO_NAME}' does not exist.")
        return False
    else:
        raise Exception(
            f"❌ Failed to check repository existence. Status: {response.status_code}, Response: {response.json()}")

    """Delete the test repository using GitHub API."""
    url = f"{GITHUB_API_BASE_URL}/repos/{GITHUB_USERNAME}/{TEST_REPO_NAME}"

    response = requests.delete(url, headers=HEADERS)

    assert response.status_code in [204, 404], f"❌ Failed to delete repo: {response.json()}"

    if response.status_code == 204:
        print(f"✅ Repository '{TEST_REPO_NAME}' deleted successfully!")
    else:
        print(f"ℹ️ Repository '{TEST_REPO_NAME}' does not exist.")


if __name__ == "__main__":
    pytest.main(["-s", "tests/api/test_delete_repo.py"])
