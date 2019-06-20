import os
import csv 

# Define the path: ./budget_data.csv
data_path = os.path.join("budget_data.csv")

# Open the file
with open(data_path, newline='') as data_file:

        budget_data = csv.reader(data_file, delimiter = ",")