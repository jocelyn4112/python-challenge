# Import files 
import os
import csv
import statistics 

#Open CSV Files
output_path = os.path.join("Resources", "budget_data.csv")
# open csv file
with open(output_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
# if printing the header
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
# start with blank lists  - How to make sure it is pulling data?
    Date = []
    Rev1 = []
    Rev2 = []
    Total = 0
    Delta = []
#For number of months - total length of months 
Total_Months = len(csvreader)

#Total Revenue - sum of revenu
for "Profit/Loss" in csvreader:  
         total += 1
#or
Total = sum(Rev1)
print(total)   

# Average Change - calcualte the delta/month and average.    
for "Profit/Loss" in csvreader:
    Rev1 = []
    Rev2 = []
    Delta = [Rev2[i]-Rev1[i] for i in xrange(min(len(Rev1), len(Rev2)))]
    
    #print (Delta)
    average = statistics.mean(Delta)
            
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




