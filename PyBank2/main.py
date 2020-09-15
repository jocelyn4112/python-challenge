# Import files 
import os
import csv

#Open CSV Files
output_path = os.path.join("Resources", "budget_data.csv")
with open(output_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=rows[0:]
    w.writerow(['Date', 'Profit/Loss'])
    for data in budget_data.csv :
        w.writerow(data)
# Printing the header?
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
# start with blank lists  - How to make sure it is pulling data?
    Date = []
    Profit/Loss = []
    Total_Rev = []
    Change_In_Rev = []
   #for total months *How to add in date column?
   Date = len(csvreader)

   #total P/L
   # sum 
    total = 0
    for "Profit/Loss" in csvreader:  
         total += 1

   # Average Change
   
    for "Profit/Loss" in csvreader:

    # M2-M1/M1 
    #   #Make 2 lists and zip together? Can I use blank lists from above?   
    .append 
   #Greatest increase 
    #max
    max(*)
    #Greatest Decrease
    #min
    min(*)
    







