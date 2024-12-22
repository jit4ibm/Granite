import requests
import json

# Set up the Ollama API endpoint
url = "http://localhost:11434/api/generate"

# Headers and payload
headers = {
    "Content-Type": "application/json"
}

data = {
    "model": "granite3.1-moe:3b",                                                  # Adjust model if needed
    "prompt": "can you tell me about India in brief?",
    "stream": False
}

try:
    # Send a POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the response is successful
    if response.status_code == 200:
        # Parse the JSON response
        resp_data = response.json()  # Automatically parses JSON response
        actual_resp = resp_data.get("response", "No response found")
        print("Actual Response:", actual_resp)
    else:
        print("POST Error:", response.status_code, response.text)
except requests.exceptions.RequestException as e:
    print("Request failed:", str(e))