import re


def readInput(file):
    seq = []
    file = open(file, "r")
    for line in file.readlines():
        seq.append(line)
    print(f'{len(seq)} lines imported.')
    return seq


def findData(seq):
    records = []
    recordTemp = []
    for item in seq:
        if re.match(r'\b', item) is not None:
            match = re.match(r'(\w+)', item)
            recordTemp.append(match.group())
        else:
            records.append(recordTemp)
            recordTemp = []
    records.append(recordTemp)  # append the last one
    print(f'{len(records)} records found.')
    return records


def makeDictionary(record):
    charCounter = {}
    for response in record:
        for char in response:
            if char in charCounter:
                charCounter[char] += 1
            else:
                charCounter[char] = 1
    return charCounter


def buildListOfDictionaries(records):
    tallies = []
    for record in records:
        tallies.append(makeDictionary(record))
    return tallies


def countAndSum(tallies):
    sum = 0
    for tally in tallies:
        sum += len(tally.keys())
    return sum


records = findData(readInput('day6-input.txt'))
tallies = buildListOfDictionaries(records)
sum = countAndSum(tallies)
print(f'The sum of all positively-answered questions is: {sum}')
