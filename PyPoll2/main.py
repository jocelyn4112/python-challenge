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
    canidates = []
    total_candidate_list = []
    candidate_votes = 0
    percent_votes = 0
    canidates_info = {}
   # Creating candidate list
    for i, row in enumerate (csvreader):
        if i == 0: 
            continue
        candidate_name = row[2]     
        if candidate_name in canidates_info.keys():
            canidates_info[candidate_name] += 1
        else:
            canidates_info[candidate_name] = 1
        total_votes = 0
    #for total votes cast by candidate 
    for candidate in canidates_info.keys():
        total_votes += canidates_info[candidate] 

#percentage each caniadite won 
    for canidate in canidates_info.keys():
        votes = canidates_info[candidate]
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.%%" 
        canidates_info[canidate] = {"Votes":votes, "Percentage":percentage}
      
   
   #This is how the tutor suggested I figure this which make smore sense but was only covered in the class before, so I didn't know if I could use it in the homework. 
    #khan_lit = list.loc[candidate  == "khan"]
    #correy_lit = list.loc[candidate  == "correy"] 
    #Li_lit = list.loc[candidate  == "li"]
Max_vote = 0
Winner = None
for canidates in canidates_info.keys(): 
    if candidate_info[canidates]["votes"] > Max_vote:
        Winner = canidates
        Max_vote = candidate_info[canidates]["votes"]
        
print ('Election Results')   
print(__________________________)
print(candidates_info.keys())
print(total_votes)
for canidates in canidates_info.keys():
    print(f'{canidates}: {candidates_info[canidates]["percentage"]} {candidate_info[candidates]["votes"]}')

print (total_votes-canidates)  
print(percent_votes)
print(Total)
print(winner_votes)
print(winner)

with open('Results.txt', 'a+') as f:
  f.write(ff)  