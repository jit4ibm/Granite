import requests

# Set up the Ollama API endpoint
OLLAMA_API_URL = "http://127.0.0.1:11434/api/version"

# Function to interact with the Granite 3.1 model
def query_granite(prompt, model="granite3.1-moe:1b"):
    payload = {
        "model": model,
        "prompt": prompt
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    return response.json().get("response")

# Retail scenario: Customer behavior analysis and recommendation
prompt = """
A customer visits our retail store and buys the following items:
1. Milk
2. Bread
3. Eggs

Based on these purchases, suggest additional items the customer might need and provide a brief reasoning.
"""

# Query the model
try:
    recommendations = query_granite(prompt)
    print("Recommendations from Granite model:")
    print(recommendations)
except Exception as e:
    print(f"An error occurred: {e}")