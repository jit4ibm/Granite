import requests
import json
import time

# Set up the Ollama API endpoint
url = "http://localhost:11434/api/generate"

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

# General function to interact with the API
def query_model(prompt, model):
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
            print(f"POST Error for model {model}:", response.status_code, response.text)
            return None, execution_time
    except requests.exceptions.RequestException as e:
        print(f"Request failed for model {model}:", str(e))
        return None, None


# List of retail prompts for various scenarios
retail_prompts = [
    # Basic recommendation
    """
    A customer visits our retail store and buys the following items:
    1. Milk
    2. Bread
    3. Eggs

    Based on these purchases, suggest additional items the customer might need and provide a brief reasoning.
    """,

    # Upselling recommendations
    """
    A customer visits the electronics section and buys a smartphone. Suggest additional items for upselling and provide reasoning for each suggestion.
    """,

    # Seasonal recommendations
    """
    During the winter season, what items should a retail store prominently display to attract customers? Provide a brief explanation for each suggestion.
    """,

    # Store layout analysis
    """
    A retail store notices customers often purchase snacks and beverages together. Suggest a layout strategy to increase sales, along with reasoning.
    """,

    # Customer loyalty
    """
    A frequent customer visits the store and buys baby products regularly. How can the store incentivize this customer to increase purchases and loyalty? Provide specific examples.
    """
]

# List of models to query
models = [
    "granite3.1-moe:1b",
    "granite3.1-dense:8b",
    "phi:latest"
]

# Query each model with each prompt and display results
for prompt in retail_prompts:
    print("\n=== New Retail Scenario ===")
    print(prompt.strip())

    for model in models:
        print(f"\nQuerying model: {model}")
        recommendations, exec_time = query_model(prompt, model)

        if recommendations:
            print(f"Recommendations from model {model}:")
            print(recommendations)
            print(f"Execution time: {exec_time:.2f} seconds")
        else:
            print(f"Failed to get recommendations for model {model}.")