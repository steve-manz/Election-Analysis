#1. Total number of votes cast - Summarize the total of ballots (Col A)
#2. A complete list of candidates who received votes 
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

import csv
dir(csv)

import os
dir(os)

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize the total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here:

    # Read the file object with the reader function.

    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes +=1

        # Print the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate,,
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking the candidate's votes
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's vote count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate



    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)








