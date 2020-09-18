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
    candidates = []
    total_candidate_list = []
    candidate_votes = 0
    percent_votes = 0
    candidates_info = {}
   # Creating candidate list
    for i, row in enumerate (csvreader):
        if i == 0: 
            continue
        candidate_name = row[2]     
        if candidate_name in candidates_info.keys():
            candidates_info[candidate_name] += 1
        else:
            candidates_info[candidate_name] = 1
        total_votes = 0
    #for total votes cast by candidate 
    for candidate in candidates_info.keys():
        total_votes += candidates_info[candidate] 

#percentage each caniadite won 
    for candidate in candidates_info.keys():
        votes = candidates_info[candidate]
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%_._%" ## How to print
        candidates_info[candidate] = {"Votes":votes, "Percentage":percentage}
      
   
        #This is how the tutor suggested I figure this which make smore sense but was only covered in the class before, so I didn't know if I could use it in the homework. 
         #khan_lit = list.loc[candidate  == "khan"]
         #correy_lit = list.loc[candidate  == "correy"] 
        #Li_lit = list.loc[candidate  == "li"]
#Calulating winner 
Max_vote = 0
Winner = None
for candidates in candidates_info.keys(): 
    if candidates_info[candidates]["Votes"] > Max_vote:
        Winner = candidates
        Max_vote = candidates_info[candidates]["Votes"]
# Print resuults         
print ('Election Results')   
print("__________________________")
print(candidates_info.keys())
print(total_votes)
for candidates in candidates_info.keys():
    print(f'{candidates}: {candidates_info[candidates]["Percentage"]} {candidates_info[candidates]["Votes"]}')
print(Max_vote)
print(Winner)

#Write to a text file 
with open('Results.txt', 'a+') as f:
    f.write('Election Results')   
    f.write("__________________________")
    f.write(candidates_info)
    f.write(total_votes)
    f.write(f'{candidates}: {candidates_info[candidates]["percentage"]} {candidate_info[candidates]["votes"]}')
    f.write(Max_votes)
    f.write("__________________________")
    f.write(Winner)