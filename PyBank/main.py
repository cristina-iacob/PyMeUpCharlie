# Modules
import os
import csv 

# Set path for file 
csvpath = os.path.join("budget_data.csv")

# Open the CSV
with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")