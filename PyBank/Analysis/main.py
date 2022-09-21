import os
import csv
#import pandas as pd

#Import CSV
csvpath = os.path.join('PyBank','Resources','budget_data.csv')
with open(csvpath) as budget_data:

    #csvtest = csv.reader(budget_data)
    csvreader = csv.DictReader(budget_data)

    #Test print CSV data with header row
    #csv_header = next(csvtest)
    #print(f"CSV Header: {csv_header}")
    #for row in csvtest:
        #print (row)

    #Create empty lists to populate
    total_months = []
    total_profit = []

    #Create inital lists for totals months & total
    for col in csvreader:
        total_months.append(col['Date'])
        total_profit.append(col['Profit/Losses'])
        #convert Profit/Losses to integer for calculation of sum/change
        total_profit_clean = [eval(i) for i in total_profit]
    
    #Creating empty lists to calculate profit changes
    current_profit = []
    prior_period_profit = []
    daily_change = []

    #Loop through each record to calc change from prior profit value
    index = 1
    for i in range(2,len(total_profit_clean)+1):
        current_profit = total_profit_clean [index]
        previous_profit = total_profit_clean [index-1]
        daily_change.append(current_profit - previous_profit)
        index = index+1

#Print Final Report
print("Financial Analysis")
print('------------------------')
print('Total Months:', len(total_months))
print('Total:','$',sum(total_profit_clean))
print('Average Change:','$',round((total_profit_clean[len(total_profit_clean)-1]-total_profit_clean[0])/(len(total_profit_clean)-1),2))
print('Greatest Increase in Profits:',total_months[daily_change.index(max(daily_change))+1],'($',max(daily_change),')')
print('Greatest Decrease in Profits:',total_months[daily_change.index(min(daily_change))+1],'($',min(daily_change),')')