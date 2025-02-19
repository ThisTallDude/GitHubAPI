import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GITHUB_API_BASE_URL = "https://api.github.com"
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Test repository name
TEST_REPO_NAME = "test-repo-scm"
