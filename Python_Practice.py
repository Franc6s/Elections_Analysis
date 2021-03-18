#Practice on how to write data on a file

import os
DataSave = os.path.join("Analysis","election_analysis.txt")
with open(DataSave,"w") as myanalysis:
    myanalysis.write("Hello World!, ")
    myanalysis.write("Arapahoe, ")
    myanalysis.write("Denver, ")
    myanalysis.write("Jefferson, ")

#**********************************************************
#to write files in a different line use \n
import os
DataSave = os.path.join("Analysis","election_analysis.txt")
with open(DataSave,"w") as myanalysis:
    myanalysis.write("Hello World!")
    myanalysis.write("\nArapahoe\nDenver\nJefferson")

#SkillDrill***********************************************
import os
DataSave = os.path.join("Analysis","election_analysis.txt")
with open(DataSave,"w") as myanalysis:
    myanalysis.write("Counties in the Election")
    myanalysis.write("\n------------------------ ")
    myanalysis.write("\nArapahoe\nDenver\nJefferson")
#-----------------*************************--------------

#Read the Elections Results on the csv file
#step 1 : Add our dependencies to open the file

import csv
import os

#step 2: 
# Assign a variable to load a file from path
DataElect = os.path.join("Resources","election_results.csv")

#Assign a variable to save file to a path
DataSave = os.path.join("Analysis","election_analysis.txt")

#Open the election results and read the file
with open(DataElect) as election_data:
#to read the csv file
    file_reader = csv.reader(election_data)
#to print each row from the csv file

    for row in file_reader:
        print(row)
#to print only the first row (important)
    #for row in file_reader:
        #print(row[0])
#to print only the header
    #headers = next(file_reader)
    #print(headers)
#to remove headers
    #headers = next (file_reader)

#TO PRINT TOTAL VOTES
import csv
import os

DataElect = os.path.join("Resources","election_results.csv")

DataSave = os.path.join("Analysis","election_analysis.txt")

total_votes = 0

with open(DataElect) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        print(total_votes)
#**********************************************************
#TO PRINT EACH CANDIDATE NAME

import csv
import os

DataElect = os.path.join("Resources","election_results.csv")

DataSave = os.path.join("Analysis","election_analysis.txt")

total_votes = 0
candidate_options = []

with open(DataElect) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
#print candidate name from each row
        candidate_name = row[2]
#add the candidate name to the candidate list
        candidate_options.append(candidate_name)
#print the candidate list
print(candidate_options)
