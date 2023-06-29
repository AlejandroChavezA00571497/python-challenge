import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

# Define variables
total_votes = 0
candidates = []
candidate_votes = {}

# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in CSV file
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Add candidate name to list of candidates if not already in list
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Count votes for each candidate
        candidate_votes[candidate_name] += 1

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")


for candidate in candidates:
    votes = candidate_votes[candidate]
    vote_percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {vote_percentage}% ({votes})")
print("-------------------------")
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("-------------------------")

# Export results to text file
output_path = os.path.join("Analysis", "election_results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        votes = candidate_votes[candidate]
        vote_percentage = round((votes / total_votes) * 100, 3)
        txtfile.write(f"{candidate}: {vote_percentage}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

