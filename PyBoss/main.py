#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:07:23 2018

@author: julianordbakk
"""


#######IMPORT CSV and append
import os
import csv

csvpath= os.path.join('employee_data1.csv')
csvpath2= os.path.join('employee_data2.csv')

# Lists to store data
empID=[]
fname=[]
lname=[]
DOB=[]
SSN=[]
state=[]

#Dictionary for states

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# file 1
#open file and read
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        # Add EmpID
        empID.append(row[0])

     # Add  first name
        namesplit=(row[1]).split(" ")
        first= namesplit[0]
        fname.append(first)
        
          # Add  last name
        namesplit=(row[1]).split(" ")
        last=namesplit[1]
        lname.append(last)
        
         # Add DOB
        DOB.append(row[2])
        
         # Add SSN
        social= f"***-**- {row[3][-4:]}"
        SSN.append(social)
        
         # Add state
        state.append(us_state_abbrev[row[4]])
       

# file 2
with open(csvpath2, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        # Add EmpID
        empID.append(row[0])

        # Add  first name
        namesplit=(row[1]).split(" ")
        first= namesplit[0]
        fname.append(first)
        
          # Add  last name
        namesplit=(row[1]).split(" ")
        last=namesplit[1]
        lname.append(last)
        
         # Add DOB
        DOB.append(row[2])
        
         # Add SSN
        social= f"***-**- {row[3][-4:]}"
        SSN.append(social)
        
         # Add state
        state.append(us_state_abbrev[row[4]])


# Zip lists together
cleaned_csv = zip(empID,fname,lname,DOB,SSN,state)

# Set variable for output file
output_file = os.path.join("employees.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    
    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name","DOB", "SSN",
                     "State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
    

