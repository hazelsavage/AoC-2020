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


def countContainers(bag, rules):
    bags = [bag]
    allowedBags = []
    while (bags):
        for bag in bags:
            moreBags = countContainers2(bag, rules)
            if moreBags:
                for container in moreBags:
                    if container not in allowedBags:
                        print(
                            f'Adding \'{container}\' to search list and allowed list.')
                        bags.append(container)
                        allowedBags.append(container)
                    else:
                        print(f'\'{container}\' was already seen/added.')
            print(f'Removing \'{bag}\' from search list.')
            bags.remove(bag)
            print(f'Running total is {len(allowedBags)}.\n')
    return len(allowedBags)


def countContainers2(bag, rules):
    moreBags = []
    bagCount = 0
    print(f'\nSearching for \'{bag}\'...')
    for rule in rules:
        if bag in rule[1]:
            bagCount += 1
            moreBags.append(rule[0])
    if bagCount != 0:
        print(f'Found {bagCount} instances of \'{bag}\' as contents.')
        return moreBags


seq = readInput('day7-input.txt')
rules = grabData(seq)
bag = 'shiny gold'
count = countContainers(bag, rules)
print(f'\n{count} bags can eventually contain at least one {bag} bag.\n')
