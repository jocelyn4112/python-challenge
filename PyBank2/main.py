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

# Average Change - calcualte the delta/month and average.    
for i,row2 in enumerate(csvreader): #this needs ot be named something that refefnces somethwer e- not sure where
    if i == 0:
        continue 
    Rev1 = []
    Rev2 = []
    Delta = [Rev2[row[1]]-Rev1[i] for i in xrange(min(len(Rev1), len(Rev2)))] 
    #print (Delta)
average = statistics.mean(Delta)
        #or
        # Average = Delta / Total_Months      
    #Greatest increase - max / month
max_change = max(Delta)
    #Greatest Decrease - min / month
min_change = min(Delta)
    

print("Financial Analysis")
print( "________________________")
print(Total_Months)
print(Total)
print(Delta)
print(average)
print(max_change)
print(min_change)




