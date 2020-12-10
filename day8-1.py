

def readInput(file):
    seq = []
    file = open(file, "r")
    for line in file.readlines():
        seq.append(line)
    print(f'\n{len(seq)} lines read in.')
    return seq


exampleInput = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6'
]


def grabData(input):
    code = []
    for line in input:
        newLine = line.split(' ')
        newLine[1] = int(newLine[1])
        code.append(newLine)
    return code


def process(code):
    accumulator = 0
    alreadyExecuted = []
    lineNum = 0
    while lineNum < len(code)-1:
        if lineNum not in alreadyExecuted:
            alreadyExecuted.append(lineNum)
            instr = code[lineNum][0]
            amount = code[lineNum][1]
            print(f'{lineNum + 1}) {instr} {amount}')
            if instr == 'acc':
                accumulator += amount
                lineNum += 1
            elif instr == 'jmp':
                lineNum += amount
                print(f'::goto line {lineNum + 1}::')
            elif instr == 'nop':
                lineNum += 1
            else:
                print('huh?')
        else:
            return accumulator


seq = readInput('day8-input.txt')
code = grabData(seq)
accumulator = process(code)
print(accumulator)
