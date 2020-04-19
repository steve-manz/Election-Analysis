# Module 3 Challenge

# Instructions:

#Make a copy of the PyPoll.py file that you used throughout this module and rename it PyPoll_Challenge.py.
# 1. Create a list for the counties.
# 2. Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
# 3. Create an empty string that will hold the county name that had the largest turnout.
# 4. Declare a variable that represents the number of votes that a county received. Hint: Inside a for loop, add an if statement to check if the county name has already been recorded. If not, add it to the list of county names.
# 5. Inside the with open() function where you are outputting the file, do the following:
# 6. Create three if statements to print out the voter turnout results similar to the results shown above.
# 7. Add the results to the output file.
# 8. Print the results to the command line.

import csv
dir(csv)

import os
dir(os)

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Create a list and dictionaries for the counties (Challenge 1)
counties = []
county_votes = {}

# Initialize the total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
candidate_votes = {}

# Largest county and largest county Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

# Winning Candidate and Winning Count Tracker
largest_county = ""
highest_count = 0
largest_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    headers = next(file_reader)

    # Print each row in the CSV file.

    # First set up a loop for the county votes
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1
        
        # Calculate the votes in each county
        county_name = row[2]

        # Calulate the votes in each county
        if county_name not in counties:
            # Add the county name to the counties[] list
            counties.append(county_name)
            # Begin tracking the candidate's votes
            county_votes[county_name] = 0
        # Add a vote to the candidate's vote count
        county_votes[county_name] += 1

    # Second set up a loop for the candidate votes
    
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1

        # Print the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate,
        # add it to the candidate list

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking the candidate's votes
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's vote count
        candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the county voting results
    for county in county_votes:
        # Retrieve vote count of a candidate.
        co_votes = county_votes[county]

        # Calculate the percentage of votes.
        county_percentage = float(co_votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {county_percentage:.1f}% ({total_votes:,})\n") 

        print(county_results)

        # Print each county, the voter count, and percentage to the
        # terminal.

        #Save the candidate results to our text file
        txt_file.write(county_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (co_votes > highest_count) and (county_percentage > largest_percentage):
            highest_count = co_votes
            largest_county = county
            largest_percentage = county_percentage

# Print the largest candidates' results to the terminal.
    largest_county_summary = (
        f"-------------------------\n"
        f": {largest_county}\n"
        f"-------------------------\n")

    print(largest_county_summary)
    
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
    # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n") 

        # Print each candidate, their voter count, and percentage to the
        # terminal.
        print(candidate_results)

        #Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

# Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

#Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)











