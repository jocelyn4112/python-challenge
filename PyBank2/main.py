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
# Printing the header?
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
# start with blank lists  - How to make sure it is pulling data?
    Date = []
    Rev1 = []
    Rev2 = []
    Total = 0
    Delta = []
 #for total months *How to add in date column?
Total_Months = len(csvreader)
#total P/L
#Total Revenue 
  
for "Profit/Loss" in csvreader:  
         total += 1
print(total)
    #Sum of Revenue

   # Average Change
   
for "Profit/Loss" in csvreader:
    Rev1 = []
    Rev2 = []
    Delta = [Rev2[i]-Rev1[i] for i in xrange(min(len(Rev1), len(Rev2)))]
    print (Delta)
            
#for Delta in 'Profit/Loss'

    # M2-M1/M1 
    #   #Make 2 lists and zip together? Can I use blank lists from above?   
   # .append 
   #Greatest increase 
    #max
max_change = max(Delta)
    #Greatest Decrease
    #min
min_change = min(Delta)
    

print("Financial Analysis")
print( "________________________")






