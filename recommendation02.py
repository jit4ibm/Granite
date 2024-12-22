import requests

# Ollama API endpoint
OLLAMA_API_URL = "http://127.0.0.1:11434/api/tags"

def query_ollama(prompt, model="granite3.1"):
    payload = {
        "model": model,
        "prompt": prompt
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json().get("response", "No response from the model")
    except requests.exceptions.RequestException as e:
        return f"Error querying Ollama: {e}"

# Example usage for a retail organization
if __name__ == "__main__":
    customer_prompt = "Suggest some top-selling gadgets for a home office."
    recommendations = query_ollama(customer_prompt)
    print("Retail Recommendations:")
    print(recommendations)
