# python-challenge
Module 3 Challenge for the Tec de Monterrey Data Analysis Bootcamp, Introduction to Python Scripting

Both Python Scripts, PyBank and PyPoll share a similar structure, both taking in information from a CSV File, applying processes to that information through looping, and printint the results to terminal in a specific format, as well as creating a .txt file with the results.

For PyBank, it takes data from a CSV with two columns: Date and Profit/Losses, and it extracts the total number of months in the dataset, the net amount of Profit/Losses, the average of changes in Profit/Losses and both greatest decrease and increase in profits over the entire period.

For PyPoll it pulls data from a CSV with Voter ID, County and Candidate, and it calculates the total number of votes cast, the list of candidates, the percentage that each candidate got from the total votes; and the number of votes, and the winner of the election.

For both files, their names are Main.py, and they exist in a folder with the name of either PyPoll or PyBank. On the same level of Main.py inside of their respective folders, there are other folders, Resources, that contains the CSV File, and Analysis, which containts the .txt output.
