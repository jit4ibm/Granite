import requests
import json
import time

# Set up the Ollama API endpoint
url = "http://localhost:11434/api/generate"

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

# Function to interact with the Granite model
def query_granite(prompt, model="granite3.1-moe:1b"):
    # Prepare the payload dynamically
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        # Record the start time
        start_time = time.time()

        # Send a POST request
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Record the end time
        end_time = time.time()

        # Calculate execution time
        execution_time = end_time - start_time

        # Check if the response is successful
        if response.status_code == 200:
            # Parse the JSON response
            resp_data = response.json()  # Automatically parses JSON response
            actual_resp = resp_data.get("response", "No response found")
            return actual_resp, execution_time
        else:
            print("POST Error:", response.status_code, response.text)
            return None, execution_time
    except requests.exceptions.RequestException as e:
        print("Request failed:", str(e))
        return None, None


# Retail scenario: Customer behavior analysis and recommendation
prompt = """
A customer visits our retail store and buys the following items:
1. Milk
2. Bread
3. Eggs

Based on these purchases, suggest additional items the customer might need and provide a brief reasoning.
"""

# Query the model
model = "granite3.1-moe:1b"  # Example model name
recommendations, exec_time = query_granite(prompt, model)

# Display the recommendations and execution time
if recommendations:
    print("Recommendations from Granite model:")
    print(recommendations)
    print(f"Execution time: {exec_time:.2f} seconds")
else:
    print("Failed to get recommendations.")
