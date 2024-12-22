import requests
import json

# Set up the Ollama API endpoint
url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

data = {
    "model": "phi",
    "prompt": "can you tell me about India in brief?",
    "stream": False
}

# Send a POST request to the Ollama API
response = requests.post(url, headers=headers, data = json.dumps(data))

# Check if the response is successful
if response.status_code == 200:
    # Parse the JSON response and extract the recommended items
    resp_text = response.text
    # Parse the JSON response
    data = json.loads(resp_text)
    actual_resp = data ['response']
    print("Actual Response:",actual_resp)
else:
    print("Error :", response.status_code,response.text)


# Try a GET request
response = requests.get(url, headers=headers, data = json.dumps(data))

if response.status_code == 200:
    print("GET Response:", response.text)
else:
    print("GET Error:", response.status_code, response.text)