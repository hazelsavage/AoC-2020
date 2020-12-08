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


def countWholeGroupYesses(record):
    charCounter = {}
    count = 0
    for response in record:
        for char in response:
            if char in charCounter:
                charCounter[char] += 1
            else:
                charCounter[char] = 1
    for value in charCounter.values():
        if value == len(record):
            count += 1
    return count


def sumWholeGroupYesses(records):
    sum = 0
    for record in records:
        sum += countWholeGroupYesses(record)
    return sum


records = findData(readInput('day6-input.txt'))
sum = sumWholeGroupYesses(records)

print(f'There were {sum} questions answered positively by whole groups.')
