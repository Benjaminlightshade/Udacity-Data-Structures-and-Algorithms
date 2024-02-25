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

textInfo = texts[0]
callInfo = calls[-1]

print("First record of texts, " + textInfo[0] + \
    " texts " + textInfo[1] + \
        " at time " + textInfo[2])

print("Last record of calls, "+ callInfo[0] + \
    " calls " + callInfo[1] + \
        " at time " + callInfo[2] + \
            ", lasting "+ callInfo[3] + \
                " seconds"
)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

