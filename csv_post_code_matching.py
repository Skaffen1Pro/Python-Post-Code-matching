#!/usr/bin/env python
import os,csv,datetime

# Log start time for performance monitoring.
print datetime.datetime.now()

# Get all .csv files in current directory
csvlist = [file for file in os.listdir('./') if file.lower().endswith('.csv')]

# Load up valid Glasgow Post Codes - first 2 Chars only in this file.
with open('glasgowPostcodesHigh.txt') as fpH:
    post_code_high_in = fpH.read().splitlines()
    post_code_high_list = [x.strip(' ') for x in post_code_high_in]

# Load up valid Glasgow Post Codes - full Post Code.
post_code_low_list=[]
with open('glasgowPostcodesLow.txt') as fpL:
    post_code_low_in = fpL.read().splitlines()
    for postcode in post_code_low_in:
        post_code_nospace = postcode.replace(' ','')
        post_code_low_list.append(post_code_nospace)
    v = 'y'
    postcode_low_dictionary = {k:v for k in post_code_low_list}

outList=[]
# Process each .csv file in the csvlist.
for file in csvlist:
    with open(file, 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        for row in csvReader:
            # Post code is in column 9 of the .CSV file.
            post_code_in = row[9]
            if post_code_in > ' ':
                post_code_in_split = row[9].split()
                post_code_in_left = post_code_in_split[0]
                post_code_in_nospace = post_code_in.replace(' ','')
                if post_code_in_left in post_code_high_list:
                   outList.append(row)
                elif post_code_in_nospace in postcode_low_dictionary:
                   outList.append(row)

# Write out full rows where we have located a valid Post Code.
with open('outList', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL)
    csvwriter.writerows(outList)

print datetime.datetime.now()
