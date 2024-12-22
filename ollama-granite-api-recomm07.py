import requests
import json
import time
import pandas as pd
import matplotlib.pyplot as plt

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
        return None, time.time() - start_time  # Return time spent till failure


# List of retail prompts for various scenarios
retail_prompts = [
    """
    A customer visits our retail store and buys the following items:
    1. Milk
    2. Bread
    3. Eggs

    Based on these purchases, suggest additional items the customer might need and provide a brief reasoning.
    """,
    """
    A customer visits the electronics section and buys a smartphone. Suggest additional items for upselling and provide reasoning for each suggestion.
    """,
    """
    During the winter season, what items should a retail store prominently display to attract customers? Provide a brief explanation for each suggestion.
    """,
    """
    A retail store notices customers often purchase snacks and beverages together. Suggest a layout strategy to increase sales, along with reasoning.
    """,
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

# Initialize an empty dictionary to store execution times
execution_data = {model: {prompt: 0 for prompt in retail_prompts} for model in models}

# Query each model with each prompt and store execution time
for prompt in retail_prompts:
    print("\n=== New Retail Scenario ===")
    print(prompt.strip())

    for model in models:
        print(f"\nQuerying model: {model}")
        recommendations, exec_time = query_model(prompt, model)

        # Store the execution time (even if the model fails, store the time spent)
        execution_data[model][prompt] = exec_time

# Convert the dictionary to a pandas DataFrame for easier manipulation
df = pd.DataFrame(execution_data)

# Display the DataFrame (this is just for debugging)
print("\nExecution Time Data (Seconds):")
print(df)

# Generate a pie chart to compare execution times by model
total_execution_time = df.sum(axis=1)

plt.figure(figsize=(8, 8))
plt.pie(total_execution_time, labels=total_execution_time.index, autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'orange'])
plt.title('Proportion of Execution Times by Model', fontsize=14)
plt.show()