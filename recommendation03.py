import requests

# Ollama API endpoint for GET request (since POST to /api/generate isn't available)
OLLAMA_API_URL = "http://127.0.0.1:11434/api/tags"  # This endpoint works with GET requests

def query_granite_tags():
    """
    Sends a GET request to fetch available tags or models.
    """
    response = requests.get(OLLAMA_API_URL)
    if response.status_code == 200:
        return response.json()  # Assuming JSON response with tags or model info
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

# Retail scenario: Suggest additional products based on purchases (though the current endpoint is for tags)
prompt = """
A customer bought the following items:
1. Bread
2. Butter
3. Milk

Suggest three additional products the customer might need, and provide a brief explanation.
"""

# Query the available tags or models (in place of querying the Granite model)
try:
    tags_data = query_granite_tags()
    print("Tags Data from Ollama API:")
    print(tags_data)  # Print the tags or model information
except Exception as e:
    print(f"An error occurred: {e}")