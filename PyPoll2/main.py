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
        percentage = (str(percentage)) + "%" 
        candidates_info[candidate] = {"Votes":votes, "Percentage":percentage}
      
#Calulating winner 
Max_vote = 0
Winner = None
for candidates in candidates_info.keys(): 
    if candidates_info[candidates]["Votes"] > Max_vote:
        Winner = candidates
        Max_vote = candidates_info[candidates]["Votes"]
# Print results         
print ('Election Results')   
print("__________________________")
print(candidates_info.keys())
print(total_votes)
for candidates in candidates_info.keys():
    print(f'{candidates}: {candidates_info[candidates]["Percentage"]} {candidates_info[candidates]["Votes"]}')
print(Max_vote)
print("Winner: " + Winner)

#Write to a text file 
with open('Results.txt', 'a+') as f:
    f.write('Election Results\n')   
    f.write("__________________________\n")
    f.write(str(candidates_info))+ "\n"
    f.write(str(total_votes)) + "\n"
    f.write(str(f'{candidates}: {candidates_info[candidates]["Percentage"]} {candidates_info[candidates]["Votes"]}')) + "/n"
    f.write(str(Max_vote)) + '\n'
    f.write(str("__________________________"))+ "\n"
    f.write(Winner)