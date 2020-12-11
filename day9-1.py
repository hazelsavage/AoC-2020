
# What is the first number that is not the sum of two of the five numbers immediately before it?

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


def grabData(seq):
    line = 0
    count = 0
    data = []
    set = []
    preambleAmount = 5
    #print(f'seq length: {len(seq)}')
    while len(data) < (len(seq)-5):
        num = seq[line]
        if count < preambleAmount:
            set.append(num)
            count += 1
            line += 1
            #print(f'line: {line}')
        elif count == preambleAmount:
            sum = num
            group = (set, sum)
            # print(group)
            data.append(group)
            count = 0
            line -= 4
            #print(f'line: {line}')
            set = []
        else:
            return 'huh?'
    return data


data = grabData(exampleInput)
for line in data:
    print(line)
