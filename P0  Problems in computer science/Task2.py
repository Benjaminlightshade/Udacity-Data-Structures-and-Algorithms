"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

telephoneNumbers = {}
longestTime = 0

for rowItem in calls:
    if rowItem[0] not in telephoneNumbers.keys():
        telephoneNumbers[rowItem[0]] = int(rowItem[3])
    else:
        newTime = telephoneNumbers[rowItem[0]] + int(rowItem[3])
        telephoneNumbers.update({rowItem[0] : newTime})
     
    if rowItem[1] not in telephoneNumbers.keys():
        telephoneNumbers[rowItem[1]] = int(rowItem[3])
    else:
        newTime = telephoneNumbers[rowItem[1]] + int(rowItem[3])
        telephoneNumbers.update({rowItem[1] : newTime})

    

# print(telephoneNumbers["(022)46574732"])

key_list = list(telephoneNumbers.keys())
val_list = list(telephoneNumbers.values())
longestTime = max(val_list)
longestTimeTel = key_list[val_list.index(longestTime)]

print(longestTimeTel + " spent the longest time, " + str(longestTime) + \
    " seconds, on the phone during September 2016.")  

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

