"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

telephoneNumbers = []

for rowItem in texts:
    if rowItem[0] not in telephoneNumbers:
        telephoneNumbers.append(rowItem[0])
    if rowItem[1] not in telephoneNumbers:
        telephoneNumbers.append(rowItem[1])

for rowItem in calls:
    if rowItem[0] not in telephoneNumbers:
        telephoneNumbers.append(rowItem[0])
    if rowItem[1] not in telephoneNumbers:
        telephoneNumbers.append(rowItem[1])

print(len(telephoneNumbers))


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
