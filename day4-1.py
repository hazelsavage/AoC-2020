
import re

msgReadfile = "\n%d lines imported."
msgFindData = "%d passports found."
msgCheckValid = "Checking passport validity:"
msgFieldSearch = "Searching for '%s' in '%s'..."
msgValidRecords = "There are %d valid passport records.\n"


def readInput(file):
    seq = []
    file = open(file, "r")
    for line in file.readlines():
        seq.append(line)
    print(msgReadfile % len(seq))
    return seq


def findData(seq):
    passports = []
    passportTemp = []
    for item in seq:
        if re.match(r'\b', item) is not None:
            match = re.findall(r'(\w{3}:[a-z0-9#]+)', item)
            for group in match:
                passportTemp.append(group)
        else:
            #print("Adding passport record: %s" % passportTemp)
            passports.append(passportTemp)
            passportTemp = []
    passports.append(passportTemp)  # append the last one
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

    if len(passport) < len(reqFields):
        valid = False
    else:
        for field in passport:
            for reqField in reqFields:
                #print(msgFieldSearch % (reqField, field))
                match = field.find(reqField)
                if match == 0:
                    count += 1
        if count == len(reqFields):
            valid = True
    # print(valid)
    return valid


passports = findData(readInput('day4-input.txt'))
validPassports = checkValidity(passports)
