import requests
import json
import time
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set up the Ollama API endpoint
url = "http://localhost:11434/api/generate"

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

# General function to interact with the API
def query_model(prompt, model):
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        start_time = time.time()
        response = requests.post(url, headers=headers, data=json.dumps(data))
        end_time = time.time()
        execution_time = end_time - start_time

        if response.status_code == 200:
            return execution_time
        else:
            print(f"POST Error for model {model}:", response.status_code, response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed for model {model}:", str(e))
        return None


# Prompt for the models
prompt = """
A customer visits our retail store and buys the following items:
1. Milk
2. Bread
3. Eggs

Based on these purchases, suggest additional items the customer might need and provide a brief reasoning.
"""

# List of models
models = ["granite3.1-moe:1b", "granite3.1-dense:8b", "phi:latest"]
execution_times = []

# Query each model and record execution time
for model in models:
    print(f"Querying model: {model}")
    exec_time = query_model(prompt, model)
    if exec_time is not None:
        execution_times.append(exec_time)
    else:
        execution_times.append(0)

# Visualize Execution Times
plt.figure(figsize=(10, 6))
plt.bar(models, execution_times, color=['blue', 'green', 'orange'])
plt.xlabel('Models', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title('Execution Time Comparison for Different Models', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
for i, v in enumerate(execution_times):
    plt.text(i, v + 0.02, f"{v:.2f}s", ha='center', fontsize=10, color='black')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Add a line chart for trends
plt.figure(figsize=(10, 6))
plt.plot(models, execution_times, marker='o', linestyle='-', color='purple', label='Execution Time')
plt.xlabel('Models', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title('Execution Time Trend Across Models', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
for i, v in enumerate(execution_times):
    plt.text(i, v + 0.02, f"{v:.2f}s", ha='center', fontsize=10, color='black')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Example repeated execution times for Boxplot
execution_time_samples = {
    "granite3.1-moe:1b": [1.23, 1.3, 1.1, 1.25, 1.27],
    "granite3.1-dense:8b": [1.56, 1.6, 1.55, 1.57, 1.54],
    "phi:latest": [0.98, 0.95, 0.88, 0.92, 0.91],
}

plt.figure(figsize=(10, 6))
plt.boxplot(execution_time_samples.values(), labels=execution_time_samples.keys(), patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'), medianprops=dict(color='red'))
plt.xlabel('Models', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title('Execution Time Distribution Across Models', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Heatmap for Correlation (Execution Time vs. Model Parameters)
model_data = {
    "granite3.1-moe:1b": {"execution_time": 1.23, "parameters": 1_000_000_000},
    "granite3.1-dense:8b": {"execution_time": 1.56, "parameters": 8_000_000_000},
    "phi:latest": {"execution_time": 0.98, "parameters": 500_000_000},
}

# Create a DataFrame
df = pd.DataFrame.from_dict(model_data, orient='index')

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title('Correlation Between Execution Time and Model Size')
plt.show()