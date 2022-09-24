import os
import csv
from collections import Counter
import sys
#import pandas as pd

#Import CSV
csvpath = os.path.join('PyPoll','Resources','election_data.csv')
with open(csvpath) as election_data:

    #csvtest = csv.reader(election_data)
    csvreader = csv.DictReader(election_data)

    #Test print CSV data with header row
    #csv_header = next(csvtest)
    #print(f"CSV Header: {csv_header}")
    #for row in csvtest:
        #print (row)

    #Create inital lists to capture candidates & total votes
    candidates = []
    total_votes = []

    #Set total vote counter to 0
    total_votes=0

    #Count total votes and list of each vote by candidate name
    for rows in csvreader:
        total_votes = total_votes+1
        candidates.append(rows['Candidate'])

    #CONCEPT BELOW TESTED BUT NOT USED
    #Capture each unique candidate in list
    # for col in csvreader:
    #     if col['Candidate'] not in candidates:
    #         candidates.append(col['Candidate'])

    #CONCEPT BELOW TESTED BUT NOT USED
    #Create dictionary to store counts by candidate
    #candidate_count = dict.fromkeys(candidates,0)

    #Create dictionary with candidates & vote counts using Counter
    vote_count = Counter(candidates)
    max_votes = max(vote_count.values())
    winner= [i for i in vote_count.keys() if vote_count[i]==max_votes]


#Print Final Results
print('Election Results')
print('-----------------------------')
print('Total Votes:', total_votes)
print('-----------------------------')
print_index = 0
for i in vote_count:
    print(list(vote_count.keys())[print_index],':',"{0:.3%}".format(list(vote_count.values())[print_index]/total_votes),'(',list(vote_count.values())[print_index],')')
    print_index = print_index+1
print('-----------------------------')
print('Winner:', winner[0])
print('-----------------------------')

#Specify the file to write to
output_path = os.path.join('PyPoll','Analysis','election_results.csv')

#Initiate sys.stdout to write to csv
sys.stdout = open(output_path, 'w')

#Write all lines to csv
print('Election Results')
print('-----------------------------')
print('Total Votes:', total_votes)
print('-----------------------------')
print_index = 0
for i in vote_count:
    print(list(vote_count.keys())[print_index],':',"{0:.3%}".format(list(vote_count.values())[print_index]/total_votes),'(',list(vote_count.values())[print_index],')')
    print_index = print_index+1
print('-----------------------------')
print('Winner:', winner[0])
print('-----------------------------')

sys.stdout.close()