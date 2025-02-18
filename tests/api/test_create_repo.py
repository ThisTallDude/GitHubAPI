from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the GITHUB_TOKEN variable
github_token = os.getenv("GITHUB_TOKEN")

# Verify if the environment variable was loaded successfully
if github_token:
    print(f"Environment variables are working! GITHUB_TOKEN: {github_token[:5]}***")
else:
    print("Error: Failed to load environment variables.")