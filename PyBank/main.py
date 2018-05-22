

#######IMPORT CSV and append
import os
import csv

csvpath= os.path.join('budget_data_1.csv')
csvpath2= os.path.join('budget_data_2.csv')


# Lists to store data
date = []
revenue = []


# file 1
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add date
        date.append(row[0])

        # Add revenue
        revenue.append(row[1])
        
# file 2
with open(csvpath2, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        # Add date
        date.append(row[0])

        # Add revenue
        revenue.append(row[1])

# Zip lists together
cleaned_csv = zip(date,revenue)

# Set variable for output file
output_file = os.path.join("budget.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write in zipped rows
    writer.writerows(cleaned_csv)



#########Create variables for summary table
    
# Total Months
months=(len(date))
#print(len(date))

# Total Revenue:
total=0
for n in range(2,len(revenue)):
    total+=int(revenue[n])

#print(total)

# Average Revenue Change

revChange = [int(revenue[n])-int(revenue[n-1]) for n in range(2,len(revenue))]
avg=sum(revChange)/float(len(revChange))
#print(revChange)
#print(avg)
 
# Greatest Increase in Revenue:

maximum=(max(revChange))
ind=(revChange.index(maximum))
maxdate= date[ind]
maxrev= revChange[ind]
#print(date[ind],revenue[ind],revChange[ind])

# Greatest Decrease in Revenue:

minimum=(min(revChange))
ind=(revChange.index(minimum))
mindate=date[ind]
minrev=revChange[ind]
#print(date[ind],revenue[ind],revChange[ind])

#Print Summary Table

print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(months))
print("Total Revenue: $" + str(total))
print("Average Revenue Change: $" + str(avg))
print("Greatest Increase in Revenue: " + str(maxdate) +" $" + str(maxrev) )
print("Greatest Decrease in Revenue: " + str(mindate) +" $" + str(minrev)  )


#### Export

import sys
sys.stdout = open('summary.txt', 'w')
print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(months))
print("Total Revenue: $" + str(total))
print("Average Revenue Change: $" + str(avg))
print("Greatest Increase in Revenue: " + str(maxdate) +" $" + str(maxrev) )
print("Greatest Decrease in Revenue: " + str(mindate) +" $" + str(minrev)  )

