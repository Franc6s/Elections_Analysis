# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_results.txt")


# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes ={}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_turnout = ""
largest_count = 0
largest_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        #Get the candidate name from each row.
        candidate_name = row[2]

        # Print the candidate name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        #add it to the candidate list.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# 4a: Write an if statement that checks that the 
#county does not match any existing county in the county list.
        if county_name not in county_list:
            # 4b : Add it to the list of counties.
            county_list.append(county_name)
            #4c  : Begin tracking the county's vote count.
            county_votes[county_name] = 0
            #5   : Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Print the candidate list.
#print(county_votes)

txt_file = open(file_to_save,"w")

    #Print the final vote count(to terminal)
election_results = (f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n\n"
    f"County Votes:\n")
print(election_results, end="")

txt_file.write(election_results)

# 6a: Write a for loop to get the county from the county dictionary.
for county_name in county_list:
    # 6b: Retrieve the county vote count.
    votes_ct = county_votes[county_name]
        
    # 6c: Calculate the percentage of votes for the county.
    votes_percent = float(votes_ct)/float(total_votes) *100

    # 6d: Print the county results to the terminal.
    county_results = (f"{county_name}:{votes_percent: .1f}% ({votes_ct: ,})\n")
    print(county_results)
    txt_file.write(county_results)

         # 6e: Save the county votes to a text file.

         # 6f: Write an if statement to determine the winning county and get its vote count.        
    if (votes_ct > largest_count) and (votes_percent > largest_percentage):
        largest_count = votes_ct
        largest_turnout = county_name
        largest_percentage = votes_percent
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout : {largest_turnout}\n"
        f"-------------------------\n")
#7 : Print the county with the largest turnout to the terminal.

print(winning_county_summary)

txt_file.write(winning_county_summary)
# 8: Save the county with the largest turnout to a text file.


    # Save the final candidate vote count to the text file.
for candidate_name in candidate_votes:
    # 6b: Retrieve the county vote count.
    votes = candidate_votes[candidate_name]
        
    # 6c: Calculate the percentage of votes for the county.
    vote_percentage = float(votes)/float(total_votes) *100

    # 6d: Print the county results to the terminal.
    candidate_results = (f"{candidate_name}:{vote_percentage: .1f}% ({votes: ,})\n")

    print(candidate_results)
    txt_file.write(candidate_results)
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_candidate_summary)
txt_file.write(winning_candidate_summary)