import sys
import os
import requests
import base64

# Ensure the root directory is in sys.path for proper imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import config variables
from config import GITHUB_API_BASE_URL, HEADERS, GITHUB_USERNAME, TEST_REPO_NAME

# Branch details
DEFAULT_BRANCH = "main"
NEW_BRANCH_NAME = "feature-branch"


def test_initialize_repo():
    """Initialize repository with a README.md file if it's empty."""
    url = f"{GITHUB_API_BASE_URL}/repos/{GITHUB_USERNAME}/{TEST_REPO_NAME}/contents/README.md"

    # Encoding "Hello World!" to Base64 (GitHub API requires Base64 content)
    content_base64 = base64.b64encode(b"# Hello World!\nThis is a test repository.").decode("utf-8")

    payload = {
        "message": "Initial commit",
        "content": content_base64,
        "branch": DEFAULT_BRANCH  # Ensure we create the file on the correct branch
    }

    response = requests.put(url, json=payload, headers=HEADERS)

    if response.status_code == 404:
        print(f"❌ Repository '{TEST_REPO_NAME}' not found. Check your username and repo name.")
        print(f"Full response: {response.json()}")
        assert False, "Repository does not exist!"

    assert response.status_code in [201, 200], f"Failed to initialize repo: {response.json()}"
    print("✅ Repository initialized with README.md")


def test_create_branch():
    """Create a new branch in the repository using the GitHub API."""
    # Get the latest commit SHA from the default branch
    repo_url = f"{GITHUB_API_BASE_URL}/repos/{GITHUB_USERNAME}/{TEST_REPO_NAME}/git/ref/heads/{DEFAULT_BRANCH}"
    response = requests.get(repo_url, headers=HEADERS)

    assert response.status_code == 200, f"Failed to fetch main branch: {response.json()}"
    sha = response.json()["object"]["sha"]

    # Create new branch
    create_branch_url = f"{GITHUB_API_BASE_URL}/repos/{GITHUB_USERNAME}/{TEST_REPO_NAME}/git/refs"
    payload = {"ref": f"refs/heads/{NEW_BRANCH_NAME}", "sha": sha}

    response = requests.post(create_branch_url, json=payload, headers=HEADERS)

    assert response.status_code == 201, f"Failed to create branch: {response.json()}"
    print(f"✅ Branch '{NEW_BRANCH_NAME}' created successfully!")
