

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
            #print(f'{lineNum + 1}) {instr} {amount}')
            if instr == 'acc':
                accumulator += amount
                lineNum += 1
            elif instr == 'jmp':
                lineNum += amount
                #print(f'::goto line {lineNum + 1}::')
            elif instr == 'nop':
                lineNum += 1
            else:
                print('huh?')
        else:
            return False

    print(accumulator)
    return True


def checkFlip(code, instr):
    changedCode = code
    lineNum = 0
    if instr == 'nop':
        repl = 'jmp'
    elif instr == 'jmp':
        repl = 'nop'
    else:
        return 'huh?'
    for line in changedCode:
        if line[0] == instr:
            print(f'changing line {lineNum+1} from {instr} to {repl}:')
            line[0] = repl
            terminates = process(changedCode)
            lineResult = [lineNum + 1, terminates]
            if terminates == True:
                return lineResult
            line[0] = instr
        lineNum += 1


seq = readInput('day8-input.txt')
code = grabData(seq)
lineChanged_Nop = checkFlip(code, 'nop')
if lineChanged_Nop != None:
    print(lineChanged_Nop)

lineChanged_Jmp = checkFlip(code, 'jmp')
if lineChanged_Jmp != None:
    print(lineChanged_Jmp)
