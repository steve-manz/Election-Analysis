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

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here:

    # Read the file object with the reader function.

    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)
    



