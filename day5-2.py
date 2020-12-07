import math
from operator import itemgetter

records = []


def readInput(file):
    codes = []
    file = open(file, "r")
    for line in file.readlines():
        codes.append(line.rstrip())
    print('%d lines imported' % len(codes))
    file.close()
    return codes


for code in readInput('day5-input.txt'):
    valid = True
    rowMin = 0
    rowMax = 127
    colMin = 0
    colMax = 7
    seatID = None
    for index in range(len(code)):
        # determine the row
        if index >= 0 and index <= 6:
            if code[index] == 'F':
                rowMax = math.floor((rowMax - rowMin) / 2) + rowMin
            elif code[index] == 'B':
                rowMin = math.ceil((rowMax - rowMin) / 2) + rowMin
            else:
                valid = False
        # determine the column
        elif index >= 7 and index <= 9:
            if code[index] == 'L':
                colMax = math.floor((colMax - colMin) / 2) + colMin
            elif code[index] == 'R':
                colMin = math.ceil((colMax - colMin) / 2) + colMin
            else:
                valid = False
        else:
            valid = False
    if valid == False:
        print('Record is invalid')
    # determine the seat ID
    seatID = (rowMin * 8) + colMin
    record = [code, rowMin, colMin, seatID]
    if valid == True:
        records.append(record)
        print(f'{record} added')
    else:
        print('Code was invalid.')


sortedRecords = sorted(records, key=itemgetter(3))
maxSeatID = sortedRecords[-1][3]
print(f'\nThe highest seat ID is {maxSeatID}.\n')

prevSeatID = None
mySeatID = None
for record in sortedRecords:
    if record == sortedRecords[0]:
        prevSeatID = record[3]
    else:
        seatID = record[3]
        if seatID != prevSeatID + 1:
            mySeatID = seatID - 1
        prevSeatID = seatID

print(f'My seat ID is {mySeatID}.')
