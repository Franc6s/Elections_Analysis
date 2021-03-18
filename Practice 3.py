import csv
import os

DataElect = os.path.join("Resources","election_results.csv")

DataSave = os.path.join("Analysis","election_analysis.txt")

total_votes = 0

candidate_options = []

candidate_votes = {}

with open(DataElect) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #Begin tracking the candidate vote count.
            candidate_votes[candidate_name]=0
            # Add a vote to that candidate's count.
            candidate_votes[candidate_name] +=1

print(candidate_votes)
