'''
Python Script made to modernize polling process of a small rural town.
We have a CSV File with three columns: Voter ID, County and Candidate

The objective is to make a script that calculates the following values:

The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote

In addition, the  final script should both print the analysis to the terminal and export a text file with the results.
'''

#First I import the necessary libraries
import os
import csv

#I create my variables
total_votes = 0
candidates = []
candidate_number = 0
candidate_votes = {}
votes = []
vote_percentage = []

#I create the access to the cvs file

csvpath = os.path.join("..", "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #I skip the header row
    csv_header = next(csvreader)

    #I loop through all rows on the file to find the number of votes
    for row in csvreader:
        total_votes = total_votes + 1

        #I get the names of the individual candidates
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_number += 1

        #I count the votes for each candidate
        candidate_votes[candidate_name] += 1

#I calculate the percentage of votes each candidate got and choose the winner
for i in candidates:
    #votes = candidate_votes[str(i)]
    #votes.append(int(candidate_votes))
    #votes.append(candidate_votes[str(i)])
    votes.append(candidate_votes[i])
    
for j in range(0,(len(candidates))):
    vote_percentage.append(round(((votes[j]/total_votes) * 100),3))
#vote_percentage = (votes / total_votes) * 100
#vote_percentage.append(round((votes[i]/total_votes) * 100), 3)

winner = max(candidate_votes, key = candidate_votes.get)




#I print the results to terminal
print("Election Results")
print("----------------")
print("Total Votes: ", total_votes)
print("----------------")
print(candidates[0], vote_percentage[0], "% ", votes[0])
print(candidates[1], vote_percentage[1], "% ", votes[1])
print(candidates[2], vote_percentage[2], "% ", votes[2])
print("----------------")
print("Winner: ", winner)

# I export results to text file
output_path = os.path.join("Analysis", "election_results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"{candidates[0]}: {vote_percentage[0]}% ({votes[0]}) \n")
    txtfile.write(f"{candidates[1]}: {vote_percentage[1]}% ({votes[1]}) \n")
    txtfile.write(f"{candidates[2]}: {vote_percentage[2]}% ({votes[2]}) \n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

