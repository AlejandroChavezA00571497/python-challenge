'''
Python Script made to analyze financial records of a company.
We have a CSV File with two columns, Date and Profit/Losses

The objective is to make a script that calculates the following values:

The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The changes in "Profit/Losses" over the entire period, and then the average of those changes
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in profits (date and amount) over the entire period

In addition, the  final script should both print the analysis to the terminal and export a text file with the results.
'''

#First I import the necessary libraries
import os
import csv

#Then I open my variables:
total_months = 0
total_pl = 0
changes_pl = []
months_list = []
pl_list = []

#I create the access to the cvs file

csvpath = os.path.join("..","Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #I skip the header row
    csv_header = next(csvreader)

    #I read each row of data after the header and make the count of months and total PL
    for row in csvreader:
        total_months = total_months + 1
        total_pl = total_pl + int(row[1])

    #I make lists that contain both all months on the file and all profits and losses.
        months_list.append(row[0])
        pl_list.append(float(row[1]))
    
    #I calculate the changes in PL
    for i in range(1,(len(months_list))):
        changes_pl.append(pl_list[i] - pl_list[i-1])
    average_change = round((sum(changes_pl) / len(changes_pl)), 2)

    #I calculate the Greatest Increases and Decreases of Profits
    greatest_increase = max(changes_pl)
    greatest_decrease = min(changes_pl)
    greatest_increase_month = months_list[changes_pl.index(greatest_increase) + 1]
    greatest_decrease_month = months_list[changes_pl.index(greatest_decrease) + 1]

#I print all results to the Terminal
print("Module 3: Financial  Analysis")
print("-----------------------------")
print("Total Months: ", total_months)
print("Total PL: $", total_pl)
print("Average Change in PL: $", average_change)
print("Greatest Increase in Profits: ", greatest_increase_month, " $", greatest_increase)
print("Greatest Decrease in Profits: ", greatest_decrease_month, " $", greatest_decrease)

#I output the results to a txt file
output_path = os.path.join("Analysis","financial_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total PL: ${total_pl}\n")
    txtfile.write(f"Average Change in PL: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} ( ${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")