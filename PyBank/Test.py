import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join("C:\\Users\\Aspire-PC\\OneDrive\\Documentos\\Data Analysis Bootcamp Tec EDX\\Challenges\\Module 3 Challenge\\python-challenge\\PyBank\\Resources\\budget_data.csv")

# Define variables
total_months = 0
total_profit_loss = 0
profit_loss = []
months = []

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        # Count total number of months included in dataset
        total_months += 1

        # Calculate net total amount of Profit/Losses over entire period
        total_profit_loss += int(row[1])

        # Create list of Profit/Losses values and list of months values
        profit_loss.append(int(row[1]))
        months.append(row[0])

    # Calculate changes in Profit/Losses over entire period and average of those changes
    change = []
    for i in range(1,len(profit_loss)):
        change.append(profit_loss[i] - profit_loss[i-1])
    average_change = sum(change) / len(change)

    # Calculate greatest increase in profits (date and amount) over entire period
    greatest_increase = max(change)
    greatest_increase_month = months[change.index(greatest_increase)+1]

    # Calculate greatest decrease in losses (date and amount) over entire period
    greatest_decrease = min(change)
    greatest_decrease_month = months[change.index(greatest_decrease)+1]

# Print analysis to terminal
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

'''
# Export analysis to text file
output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

    '''