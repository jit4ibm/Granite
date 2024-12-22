 # Assisted by watsonx Code Assistant 
import pandas as pd

def load_data_from_csv_using_pandas(file_path):
    try:
        print(f"Loading data from: {file_path}")
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    

file_path = 'import_files/TrafficIndex_19Jun2024-26Jun2024.csv'
data = load_data_from_csv_using_pandas(file_path)
if data is not None:
    data.head()
    print(data)
else:
    print("No data loaded.")