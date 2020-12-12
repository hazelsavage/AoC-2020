
# What is the first number that is not the sum of two of the five numbers immediately before it?


def readInput(file):
    seq = []
    file = open(file, "r")
    for line in file.readlines():
        seq.append(int(line.rstrip()))
    print(f'{len(seq)} lines read in.')
    return seq


# example has 5 preamble lines, then each number should be the sum of two of the preceeding five numbers
exampleInput = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576
]


def grabData(seq, preambleAmount):
    line = 0
    count = 0
    data = []
    set = []
    #print(f'seq length: {len(seq)}')
    while len(data) < (len(seq)-preambleAmount):
        num = seq[line]
        if count < preambleAmount:
            set.append(num)
            count += 1
            line += 1
            #print(f'line: {line}')
        elif count == preambleAmount:
            sum = num
            group = [set, sum]
            # print(group)
            data.append(group)
            count = 0
            line -= preambleAmount - 1
            #print(f'line: {line}')
            set = []
        else:
            return 'huh?'
    print(f'\n{len(data)} preamble & number sets found.')
    return data


def doMaths(data):
    count = 0
    checkedData = data
    for line in checkedData:
        for num1 in line[0]:
            for num2 in line[0]:
                if (num1 + num2 == line[1]) and (num1 != num2):
                    if True not in line:
                        line.append(True)
                        count += 1
                    # print(line)
    print(f'{count} \'sum\' sets found.')
    return checkedData


def search(checkedData):
    noSums = []
    for line in checkedData:
        if True not in line:
            noSums.append(line)
    return noSums


#seq = readInput('day9-input.txt')

data = grabData(exampleInput, 5)
checkedData = doMaths(data)
noSums = search(checkedData)
print(f'The first \'no-sum\' number is {noSums[0][1]}.\n')
