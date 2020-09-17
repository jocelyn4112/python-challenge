import os
import csv
import statistics 

output_path = os.path.join("Resources", "election_data.csv")
# open csv file
with open(output_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
 #Blank Lists and variables 
    total_votes = 0
    # List of canidates 
    total_candidate_list = []
    # Number of votes each canidate recieves 
    candidate_votes = []
    Percent_Votes = []
#for total votes cast 
for Total_votes in csvreader:
     Total =+ 1
    #Compiling total canidates and votes - if candidate is not on the list of canidates they and their votes are added on.  
if row[2] not in total_candidate_list:      
        total_candidate_list.append.row[2]
        index = total_candidate_list.index(row[2])
        total_votes.append(1)
else:
        index = total_candidate_list.index(row[2])
        total_votes[index] += 1
    print(total_candidate_list)
    print(total_votes)
    #Make Index Canidate List
    candidateIndex = candidates.index(row[2])
     # Index to count of votes for the candidate
    total_votes = [candidateIndex] += 1
    #percentage each caniadite won 
        #Sum each cannidates votes - Citation?
       # for votes in total_candidates:
        #    percentage = (votes/total_votes) * 100
         #   percentage = round(percentage)
          #  percentage = "%.3f%%" % percentage
           # percent_votes.append(percentage)
        #Divide by total votes
               # /Total_votes
    #Total muber for votes for each canidate 
    for row in csvreader:
        if row[0] == candidate:
            Total =+ 1
         #Sum Canidates A,B,C
    #winner
   
    
print(Total)



   