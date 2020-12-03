import re

seq = []
valid = 0
msg_result = "\nThere are %d valid passwords.\n"


file = open('day2-input.txt', 'r')
for line in file.readlines():
    getRecord = re.match(r'(\d+)-(\d+)\s(\w):\s(\w+)', line.rstrip())
    seq.append(getRecord.groups())

for record in seq:
    lb = int(record[0])
    ub = int(record[1])
    letter = record[2]
    count = 0
    pw = record[3]
    for char in pw:
        if char == letter:
            count += 1
    if count >= lb and count <= ub:
        valid += 1


print(msg_result % valid)


# for each line:

# pull out the letter, save it in a variable.
# make a 2-item array with the lower and upper bounds of how often that letter's allowed.
# pull out the actual password.
# (regular expressions?)

# loop through the password string one character at a time,
# make a note each time you encounter the saved letter.

# check the letter count var against the lower and upper bounds specified for it.
# If the letter count is >= the lower bound and <= the upper bound,
# then increment a 'valid passwords' variable.
# The 'valid passwords' variable (after all the lines are checked) will be the answer.
