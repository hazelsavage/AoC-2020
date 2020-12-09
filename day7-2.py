import re


def readInput(file):
    seq = []
    file = open(file, "r")
    for line in file.readlines():
        seq.append(line)
    print(f'\n{len(seq)} lines read in.')
    return seq


def grabData(seq):
    rules = []
    for line in seq:
        str_0 = line.split(' bags contain ')
        container = str_0[0]
        contents = str_0[1]
        contents = grabData2(contents)
        rule = [container, contents]
        rules.append(rule)
    return rules


def grabData2(contents):
    contents = contents.split(', ')
    newContents = {}
    for content in contents:
        newContent = content.split(' bag')[0]
        if newContent == 'no other':
            newContents['no other'] = 0
        else:
            matches = re.match(r'(\d+)\s(\w+\s\w+)', newContent)
            groups = matches.groups()
            newContents[groups[1]] = int(groups[0])
    return newContents


def countBagsInside(outerBag, rules):
    bagsToCheck = [outerBag]
    for bag in bagsToCheck:
        for rule in rules:
            if bag in rule[0]:
                for item in rule[1].items():
                    for i in range(item[1]):
                        bagsToCheck.append(item[0])
    bagsToCheck.remove(outerBag)
    insideBags = bagsToCheck
    return len(insideBags)


seq = readInput('day7-input.txt')
rules = grabData(seq)
outerBag = 'shiny gold'
insideBagsCount = countBagsInside(outerBag, rules)

print(insideBagsCount)
