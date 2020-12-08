import re

# read the rules in (there is one rule per line)

# use regex to pickup the key information.

# make a dictionary for each rule:
# e.g. muted_lime {
#   wavy_lime: 1,
#   vibrant_green: 1
#    light_yellow: 3
# }

# Then what...?

exampleInput = [
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.'
]


def grabData(records):
    rules = []
    for record in records:
        split1 = record.split(' bags contain ')
        for string in split1:
            split2 = string.split(', ')
            print(split2)
    return rules


grabData(exampleInput)
