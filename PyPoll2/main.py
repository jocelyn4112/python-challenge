import os
import csv

output_path = os.path.join("Resources", "election_data.csv")
# open csv file
with open(output_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    Total_votes = 0
    total_candidates = []
    candidate_votes = []
  #for total votes cast 
    for Total_votes in csvreader:
        Total =+ 1
    #for list of canidates 
        if row[0] not in total_candidates:      
            total_candidates.append.row[0]
    #percentage each caniadite won 
        #Sum each cannidates votes

        #Divide by total votes
                /Total_votes
    #total muber for votes for each canidate 
     for row in csvreader:
        if row[0] == canidate:
            Total =+ 1
         #Sum Canidates A,B,C
    #winner
   
    
    print(Total)



   