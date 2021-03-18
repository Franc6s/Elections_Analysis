#Reading a file with Python|direct path**********

#import csv

## csv_reader = csv.reader(DataElect)

    #for line in csv_reader:
       # print(line)
#**********************************************************
#Writing in file with Python with statements*******

#step 1
#import os

#step2
#Statement to open the file as a text file

#DataSave = os.path.join("Analysis","election_analysis.txt")

#myanalysis = open(DataSave,"w")

#step 3
#Writing some data to the file
#myanalysis.write("Hello World!")

#step 4
#Close the file when done
#myanalysis.close()
#**********************************************************
#Writing a file in python using the "with" statement*********

#DataSave = os.path.join("Analysis","election_analysis.txt")

#using the "with" statement to open the file as text file

#with open(DataSave,"w") as myanalysis:
    #myanalysis.write("Hello World!")
#******************************************************
import csv
import os

DataElect = os.path.join("Resources","election_results.csv")

DataSave = os.path.join("Analysis","election_analysis.txt")

total_votes = 0

candidate_options = []

candidate_votes = {}

#Last Step
#Winning candidate and winning count tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(DataElect) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:
            total_votes +=1
#Print the candidate name from each row
            candidate_name = row[2]
#Add the candidate name to the candidate list
            if candidate_name not in candidate_options:
                    candidate_options.append(candidate_name)
#Create each candidate as a key and to begin tracking a candidate's vote count
                    candidate_votes[candidate_name]= 0
#To add a vote to that candidate's count
            candidate_votes[candidate_name] += 1
#To determine the percentage of votes for each candidate           
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
            #to get a percentage, convert votes and total_votes to floating-point
            #because in the dictionary, votes and total votes are integer
        vote_percentage = float(votes)/float(total_votes)*100

                #determine if the votes are greater than the winning count
        if(votes>winning_count) and (vote_percentage>winning_percentage):

                #if true then set winning count = votes
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
#to do: print out the winning candidate, vote count and percentage to terminal.
    Winnin_candidate_summary = (
            f"-----------------------------\n"
            f"Winner : {winning_candidate}\n"
            f"Winning Vote Count : {winning_count:,}\n"
            f"Winning Percentage :{winning_percentage:.1f}%\n"
            f"------------------------------\n")        
    
    print(Winnin_candidate_summary)

