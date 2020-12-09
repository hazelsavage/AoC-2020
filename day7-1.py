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


def countAllContainers(bag, rules):
    count = 0
    oldCount = None
    bag2 = None
    loopNum = 0
    while (count != oldCount):  # did the counter increase - i.e., did we find a new instance last time?
        oldCount = count
        loopNum += 1
        print(f'\nloop {loopNum}:')
        if bag2 != None:
            bag = bag2
        print(f'searching for {bag} bag:')
        for rule in rules:
            if bag in rule[1]:  # is the bag in the dictionary for this container rule?
                print(rule)
                count += 1
                # search for the container bag in other containers' dictionaries next time.
                bag2 = rule[0]
    return count

    # at present, subsequent loops of the above function only look for
    # the most recent container bag, and so our answer is wrong!
    # We need a list of container bags and too look for all of them, one at a time.
    # (And to take each one off the list when we're done looking for that one.)


seq = readInput('day7-input.txt')
rules = grabData(seq)
bag = 'shiny gold'
count = countAllContainers(bag, rules)
print(f'\n{count} bags can eventually contain at least one {bag} bag.\n')
