# Import files 
import os
import csv
import statistics 

#Open CSV Files
output_path = os.path.join("Resources","budget_data.csv")
# open csv file
with open(output_path) as csvfile:
    csvreader = csv.reader(csvfile)
 
    #for row in csvreader:
    #    print(row)

    # if printing the header
    csv_header = next(csvreader)
    print("CSV Header:", csv_header) 

    Rev1 = "Profit/Loss" 
# start with blank lists  - How to make sure it is pulling data?
    Date = []
    Rev1 = []
    Rev2 = []
    total = 0
    Delta = []
#For number of months = total length of months (points back to csv file  
    Total_Months = len("Months")
    #print(Total_Months)
#Total Revenue - sum of revenue
    for Rev1 in csvreader:  
         total += 1
#or
#Total = sum(Delta)
    #print(total)   

# Average Change - calcualte the delta/month and average. (M2-M1)/M1    
    for i,row2 in enumerate(csvreader): 
        if i == 0:
            continue 
        Rev1 = []
        Rev2 = []
        Delta = [Rev2[row[1]]-Rev1[i] for i in range(min(len(Rev1), len(Rev2)))] 
    
    #average = statistics.mean([Delta])
        #or
    #average =Delta/ Total_Months     
    #Greatest increase - max / month
    #max_change = max(Delta)
    #Greatest Decrease - min / month
    #min_change = min(Delta)
    
#Print results
print("Financial Analysis")
print( "________________________")
print(Total_Months)
print(total)
print(Delta)
print(average)
print(max_change)
print(min_change)

#Write to text file
with open ("Results", "w") as f:   
    f.write(str('Results'))+ "\n"
    f.write(str( "________________________") + "\n"
    f.write(str(Total_Months)) + "\n"
    f.write(str(Total)) + "\n"
    f.write(str(Delta)) + "\n"
    f.write(str(average)) + "\n"
    f.write(str(max_change)) + "\n"
    f.write(str(min_change)) + "\n"
    




