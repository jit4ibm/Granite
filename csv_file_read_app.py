# Assisted by watsonx Code Assistant 
import csv

def load_data_from_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

file_path = 'import_files/TrafficIndex_19Jun2024-26Jun2024.csv'
data = load_data_from_csv(file_path)
if data is not None:
    print(data)
else:
    print("No data loaded.")
