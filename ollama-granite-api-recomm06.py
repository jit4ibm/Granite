import requests
import json
import time
import matplotlib.pyplot as plt
import pandas as pd

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

# Retail scenario: Customer behavior analysis and recommendation
prompt = """
A customer visits our retail store and buys the following items:
1. Milk
2. Bread
3. Eggs

Based on these purchases, suggest additional items the customer might need and provide a brief reasoning.
"""

# List of models to query
models = [
    "granite3.1-moe:1b",
    "granite3.1-dense:8b",
    "phi:latest"
]

# Store execution times in a dictionary
execution_times = {model: 0 for model in models}
failure_times = {model: 0 for model in models}

# Query each model and record execution time
for model in models:
    print(f"\nQuerying model: {model}")
    recommendations, exec_time = query_model(prompt, model)

    # Record the execution time (either success or failure)
    execution_times[model] = exec_time if exec_time else 0
    failure_times[model] = exec_time if exec_time else time.time() - time.time()  # Time spent even if failed

    if recommendations:
        print(f"Recommendations from model {model}:")
        print(recommendations)
        print(f"Execution time: {exec_time:.2f} seconds")
    else:
        print(f"Failed to get recommendations for model {model}. Execution time recorded: {failure_times[model]:.2f} seconds")

# Create a dataset from the execution times
df = pd.DataFrame(list(execution_times.items()), columns=["Model", "Execution Time"])
df["Failure Time"] = df["Model"].map(failure_times)

# Display execution times
print("\nModel-wise Execution Times:")
print(df)

# Pie chart visualization of the execution times
plt.figure(figsize=(8, 8))
plt.pie(df['Execution Time'], labels=df['Model'], autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'orange'])
plt.title('Proportion of Execution Times by Model')
plt.show()

# If models fail, use the failure time in the pie chart instead
plt.figure(figsize=(8, 8))
plt.pie(df['Failure Time'], labels=df['Model'], autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'orange'])
plt.title('Proportion of Time Spent (Including Failures) by Model')
plt.show()