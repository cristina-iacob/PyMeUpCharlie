import os
import csv

csvpath = os.path.join('budget-data.csv')

#list to store data
monthList = []
revenueList = []
monthlyChanges = []
monthlyChanges_for_month = []


# Module for reading CSV files
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # read each row of data
    for row in csvreader:
        #build up monthList
        monthList.append(row[0])
        #build up revenueList
        revenueList.append(float(row[1]))

    # number of months in the list
    monthCount = len(monthList)

    # calculate the total revenue
    revenueTotal = sum(revenueList)


    # calculate greatest increase in revenue
    highRevenue = 0
    for i in range(len(revenueList)):
        if int(revenueList[i]) - int(revenueList[i - 1]) > highRevenue:
            highRevenue = int(revenueList[i]) - int(revenueList[i- 1])
            highMonth = monthList[i]

    for k in range(len(revenueList)-1):
        monthlyChanges.append(revenueList[k + 1] - revenueList[k])
        monthlyChanges_for_month.append(monthList[k])
    # calculate average change in revenue over the entire period rounded to 2 decimal places
    #averageChange = round(float((max(revenueList) - min(revenueList)) / monthCount),2)
    averageChange = round(sum(monthlyChanges)/len(monthlyChanges), 2)

    # calculate greatest decrease in revenue
    lowRevenue = 0
    for j in range(len(revenueList)):
        if int(revenueList[j]) - int(revenueList[j - 1]) < lowRevenue:
            lowRevenue = int(revenueList[j]) - int(revenueList[j - 1])
            lowMonth = monthList[j]

    displayData = ("Financial Analysis \n" )
    displayData += ("-------------------------------------\n")
    displayData += ("Total Months: " + str(monthCount) + "\n")
    displayData += ("Total: $"  + str(round(revenueTotal)) + "\n")
    displayData += ("Average Change: $" + str(averageChange)+ "\n")
    displayData += ("Greatest Increase in Profits: " + str(highMonth) + " " + "($" + str(highRevenue) + ")" + "\n")
    displayData += ("Greatest Decrease in Profits: " + str(lowMonth) + " " + "($" + str(lowRevenue) + ")"+ "\n")

# Set variable for output file
#output_file = os.path.join("budget_results.txt")

# Open the output file
#with open(output_file, "w") as file:
#   writer = csv.writer(datafile)

    # Write in budget_results.txt file requested info
    #file.write("--------------------------------------------------- \n")
    #file.write("Financial Analysis \n")
    #file.write("--------------------------------------------------- \n")
    #file.write("Total Months: " + str(monthCount) + "\n")
    #file.write("Total: $"  + str(round(revenueTotal)) + "\n")
    #file.write("Average Change: $" + str(averageChange) + "\n")
    #file.write("Greatest Increase in Profits: " + str(highMonth) + " " + "($" + str(highRevenue) + ")" + "\n")
    #file.write("Greatest Decrease in Profits: " + str(lowMonth) + " " + "($" + str(lowRevenue) + ")" + "\n")
    #file.write ("--------------------------------------------------- \n")

print(displayData)
file = open('budget_results.txt',"w")
file.write(displayData)
file.close()