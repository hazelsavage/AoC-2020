from functools import reduce


def readInput(file):
    seq = []
    file = open(file, "r")
    for line in file.readlines():
        seq.append(int(line.rstrip()))
    print(f'{len(seq)} lines read in.')
    return seq


exampleInput = [
    # example has 5 preamble lines, then each number
    # should be the sum of two of the preceeding five numbers
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


def part1(seq, preambleAmount):

    def grabData(seq, preambleAmount):
        line = 0
        count = 0
        data = []
        set = []
        # print(f'seq length: {len(seq)}')
        while len(data) < (len(seq)-preambleAmount):
            num = seq[line]
            if count < preambleAmount:
                set.append(num)
                count += 1
                line += 1
                # print(f'line: {line}')
            elif count == preambleAmount:
                sum = num
                group = [set, sum]
                # print(group)
                data.append(group)
                count = 0
                line -= preambleAmount - 1
                # print(f'line: {line}')
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

    invalidNum = search(doMaths(grabData(seq, preambleAmount)))[0][1]
    print(f'{invalidNum} is the invalid number.')
    return invalidNum


def part2(seq, invalidNum):

    def findRange(seq, invalidNum):
        i = 0
        iMax = seq.index(invalidNum)
        j = 0
        while (j < iMax):
            testSet = []
            for i in range(j, iMax):
                testSet.append(seq[i])
                sum = reduce(lambda a, b: a+b, testSet)
                if sum == invalidNum:
                    return testSet
                elif sum > invalidNum:
                    j += 1
                    break
                else:
                    continue

    def solve(foundRange):
        result = min(foundRange) + max(foundRange)
        return result

    foundRange = findRange(seq, invalidNum)
    result = solve(foundRange)
    return result


seq = readInput('day9-input.txt')
preambleAmount = 25
invalidNum = part1(seq, preambleAmount)
result = part2(seq, invalidNum)

print(
    f'The sum of the smallest and largest numbers in the range that sums to {invalidNum} is {result}.')
