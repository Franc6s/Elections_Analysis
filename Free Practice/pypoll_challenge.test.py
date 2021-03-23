import csv
import os

DataElect = os.path.join("Resources","election_results.csv")

DataSave = os.path.join("Analysis","election_analysis.txt")

total_votes = 0

county_list = []

county_votes = {}

with open(DataElect) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if county_name not in county_list:
            # Add it to the list of candidates.
            county_list.append(county_name)

            county_votes[county_name] = 0

        county_votes[county_name] += 1

# Print the candidate list.
print(county_votes)