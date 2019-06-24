import os
import csv

csvpath = os.path.join('election_data.csv')

# Assign initial values
total_votes = 0
winner_count = 0

#Assign dictionaries to store data
candidates = {}
candidates_percent = {}


# Module for reading CSV files
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_votes += 1

        #Get Candidate Names
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        #print(candidates)

        #Compute percentage looping over both key (candidate) and value
        for key, value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 3)
        #print(candidates_percent[key])

        #Find the winner
        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]

# Write to the terminal requested info: Election Results, Total Votes, percentages and Winner
print ("Election Results")
print ("-------------------------------------")
print ("Total Votes:" + str(total_votes))
print ("-------------------------------------")
for key, value in candidates.items():
    print (key + ":" + str(candidates_percent[key]) + "% (" + str(value) + ")")
print ("-------------------------------------")
print ("Winner: " + winner)
print ("-------------------------------------")

# Set variable for output file
output_file = os.path.join("pollresults.txt")

# Open the output file
with open(output_file, "w") as file:
#   writer = csv.writer(datafile)

# Write in  pollresults.txt file requested info: Election Results, Total Votes, percentages and Winner
    file.write("Election Results \n")
    file.write("-------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("-------------------------------- \n")
    for key, value in candidates.items():
        file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    file.write("---------------------------------\n")
    file.write("Winner: " + winner + "\n")
    file.write("--------------------------------- \n")
