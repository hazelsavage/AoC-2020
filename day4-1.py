
import re

msgReadfile = "\n%d lines imported."
msgFindData = "%d passports found."
msgCheckValid = "Checking passport validity:"
msgFieldSearch = "Searching for '%s' in '%s'..."
msgValidRecords = "There are %d valid passport records.\n"

# The validity functions are fine, but we are reading
# in the data wrongly, as fields for each passport are spread
# over several lines.

# We need to split the data into passports as we read it in,
# appending everything upto each newline as one record in our list.


def readInput(file):
    seq = []
    file = open(file, "r")
    for line in file.readlines():
        seq.append(line.rstrip())
    print(msgReadfile % len(seq))
    return seq


def findData(seq):
    passports = []
    for item in seq:
        if len(item) > 1:
            match = re.findall(r'(\w{3}:[a-z0-9#]+)', item)
            passports.append(match)
    print(msgFindData % len(passports))
    return passports


def checkValidity(passports):
    validPassports = []
    valid = False

    for passport in passports:
        valid = checkPassportFields(passport)
        if valid == True:
            validPassports.append(passport)
    print(msgValidRecords % len(validPassports))
    return validPassports


def checkPassportFields(passport):
    # print(msgCheckValid)
    count = 0
    valid = False
    reqFields = [
        'byr',  # Birth Year
        'iyr',  # Issue Year
        'eyr',  # Expiration Date
        'hgt',  # Height
        'hcl',  # Hair Color
        'ecl',  # Eye Color
        'pid',  # Passport ID
        # 'cid' #Country ID (expected but not currently required)
    ]

    if len(passport) < 7:
        valid = False
    else:
        for field in passport:
            for reqField in reqFields:
                #print(msgFieldSearch % (reqField, field), end=" ")
                match = field.find(reqField)
                if match == 0:
                    count += 1
        if count == len(reqFields):
            valid = True
    print(valid)
    return valid


passports = findData(readInput('day4-input.txt'))
validPassports = checkValidity(passports)
