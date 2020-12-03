import re

seq = []
valid = 0
msg_test = "\nTesting for '%s' at positions %d and %d of %s..."
msg_pass = "Yep! Position %d."
msg_fail = "Nope."
msg_result = "\nThere are %d valid passwords.\n"


file = open('day2-input.txt', 'r')
for line in file.readlines():
    getRecord = re.match(r'(\d+)-(\d+)\s(\w):\s(\w+)', line.rstrip())
    seq.append(getRecord.groups())

for record in seq:
    pos1 = int(record[0])
    pos2 = int(record[1])
    letter = record[2]
    pw = record[3]
    print(msg_test % (letter, pos1, pos2, pw), end=" ")
    if (pw[pos1 - 1] == letter) ^ (pw[pos2 - 1] == letter):
        valid += 1
        if pw[pos1 - 1] == letter:
            print(msg_pass % pos1)
        elif pw[pos2 - 1] == letter:
            print(msg_pass % pos2)
    else:
        print(msg_fail)


print(msg_result % valid)
