#Reading a file with Python|direct path**********

import csv

with open('Resources\election_results.csv','r') as DataElect:
    csv_reader = csv.reader(DataElect)

    for line in csv_reader:
        print(line)
#**********************************************************
#Writing in file with Python with statements*******

#step 1
import os

#step2
#Statement to open the file as a text file

DataSave = os.path.join("Analysis","election_analysis.txt")

myanalysis = open(DataSave,"w")

#step 3
#Writing some data to the file
myanalysis.write("Hello World!")

#step 4
#Close the file when done
myanalysis.close()
#**********************************************************
#Writing a file in python using the "with" statement*********

DataSave = os.path.join("Analysis","election_analysis.txt")

#using the "with" statement to open the file as text file

with open(DataSave,"w") as myanalysis:
    myanalysis.write("Hello World!")
#******************************************************
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