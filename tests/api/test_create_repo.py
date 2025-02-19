import requests
import sys
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Now import the config
from config import GITHUB_API_BASE_URL, HEADERS, TEST_REPO_NAME


def test_create_repository():
    """Create a new repository using GitHub API."""
    url = f"{GITHUB_API_BASE_URL}/user/repos"
    payload = {"name": TEST_REPO_NAME, "private": False}

    response = requests.post(url, json=payload, headers=HEADERS)

    assert response.status_code in [201, 422], f"Failed to create repo: {response.json()}"

    if response.status_code == 201:
        print(f"✅ Repository '{TEST_REPO_NAME}' created successfully!")
    else:
        print(f"ℹ️ Repository '{TEST_REPO_NAME}' already exists.")
