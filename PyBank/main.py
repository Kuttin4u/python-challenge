#Import commands
import os
import csv

#Set path for file 
budget_path = os.path.join('Resources','budget_data.csv')

#CSV to read

with open(budget_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Print....[CSV Header: CVS Header]
    csv_header=next(csvreader)
    

    #Variables to output
    row=(0,1)
    total_months = row[0] 
    net_profit_loss=row[1] 
    average_loss= row[1]
    gincrease = ["", 0]
    gdecrease = ["", 9999999999999999999999]
    budget_output = (total_months, net_profit_loss, average_loss, gincrease, gdecrease) 

        #Loop through dataset 
    for row in csvreader:
        print(row)
        
    #Run calcualation for totals
        if row[0]== total_months: (row[0], 86)
        print(total_months) 
        if row[1]== net_profit_loss: total=sum(row[1])
        print(net_profit_loss) 
        if row[1]== average_loss: total= avg(int(row[1]))
        print(average_loss)
        if row[1]== gincrease: total= max(long(row[1]))
        print(gincrease)
        if row[1]== gdecrease: total= min(long(row[1]))          
        print(gdecrease)        
    
        # Print output of data requested
        print(budget_output)

 