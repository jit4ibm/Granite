from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve the API URL
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL")

if not OLLAMA_API_URL:
    raise ValueError("OLLAMA_API_URL is not set in the .env file.")