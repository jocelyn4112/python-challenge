# Import Dependencies 
import os
import csv
import statistics 
# open csv file
output_path = os.path.join("Resources", "election_data.csv")
with open(output_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
 #Blank Lists and variables 
    total_votes = 0
    total_candidate_list = []
    candidate_votes = 0
    percent_votes = 0
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

#Make Index Canidate List
    candidateIndex = candidates.index(row[2])
# Index to count of votes for the candidate
    total_votes = [candidateIndex] += 1
#Total muber for votes for each canidate 
    for row in csvreader:
        if row[0] == candidate:
            Total =+ 1
#percentage each caniadite won 
    for votes in total_candidates:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.%%" 
        percent_votes.append(percentage)
      
   
   #This is how the tutor suggested I figure this which make smore sense but was only covered in the class before, so I didn't know if I could use it in the homework. 
    #khan_lit = list.loc[candidate  == "khan"]
    #correy_lit = list.loc[candidate  == "correy"] 
    #Li_lit = list.loc[candidate  == "li"]

   for winner in candidate_votes   
     if vote_count > winner_votes:
        winner = vote_count
        winner = 
        
   
print(total_candidate_list)
print(total_votes) 
print (total_votes-canidates)  
print(percent_votes)
print(Total)
print(winner_votes)


   