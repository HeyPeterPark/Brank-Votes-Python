#PyBank

import csv
from csv import reader

#Header: [Date, Profit/Losses] - [Jan-2010, 867884]
opened_file = open("Resources/budget_data.csv", encoding ="utf-8")
read_file = reader(opened_file)
budget_data = list(read_file)

date = []
net_change = []
rev_change = [0,]

#dates and profit/losses in separate lists
for row in budget_data[1:]:
    date.append(row[0])
    net_change.append(float(row[1]))

#net change(s)
for row in range(1,len(net_change)):
    rev_change.append(net_change[row] - net_change[row - 1])   
    avg_rev_change = sum(rev_change) / ((len(rev_change)) - 1)

    max_rev_change = max(rev_change)
    min_rev_change = min(rev_change)

    max_rev_change_date = date[rev_change.index(max(rev_change))]
    min_rev_change_date = date[rev_change.index(min(rev_change))]

#print statement
summ_pybank = f'''
Financial Analysis
{'-'*30}
Total Months: {len(date)}
Total: ${int(sum(net_change))}
Average Change: ${round(avg_rev_change,2)}
Greatest Increase in Profits: {max_rev_change_date} (${int(max_rev_change)})
Greatest Decrease in Profits: {min_rev_change_date} (${int(min_rev_change)})
'''

print(summ_pybank)

#exporting
textfile = open('PyBank.txt', 'w')
textfile.write(summ_pybank)
textfile.close()
