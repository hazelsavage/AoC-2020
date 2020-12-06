
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
            # print("Adding passport record: %s" % passportTemp)
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
                # print(msgFieldSearch % (reqField, field))
                match = field.find(reqField)
                if match == 0:
                    if fieldCheckSelector(reqField, field) == True:
                        count += 1
                if count == len(reqFields):
                    valid = True
    # print(valid)
    return valid


def fieldCheckSelector(reqField, field):
    data = field.split(':')[1]
    if reqField == 'byr':
        return byrCheck(data)
    elif reqField == 'iyr':
        return iyrCheck(data)
    elif reqField == 'eyr':
        return eyrCheck(data)
    elif reqField == 'hgt':
        return hgtCheck(data)
    elif reqField == 'hcl':
        return hclCheck(data)
    elif reqField == 'ecl':
        return eclCheck(data)
    elif reqField == 'pid':
        return pidCheck(data)
    else:
        return None


def byrCheck(data):  # birth year check
    valid = False
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if int(data) >= 1920 and int(data) <= 2002:
        valid = True
    return valid


def iyrCheck(data):  # issue year check
    valid = False
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if int(data) >= 2010 and int(data) <= 2020:
        valid = True
    return valid


def eyrCheck(data):  # expiration year check
    valid = False
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if int(data) >= 2020 and int(data) <= 2030:
        valid = True
    return valid


def hgtCheck(data):  # height check
    valid = False
    # hgt (Height) - a number followed by either cm or in:
    # If cm, number >= 150 and <= 193.
    # If in, number >= 59 and <= 76.
    match = re.match(r'(\d*)(in|cm)', data)
    if match is not None:
        num = int(match[1])
        # print(num)
        units = str(match[2])
        # print(units)
        if units == "cm":
            if num >= 150 and num <= 193:
                valid = True
        elif units == "in":
            if num >= 59 and num <= 76:
                valid = True
    else:
        valid = False
    return valid


def hclCheck(data):  # hair color check
    valid = False
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    match = re.match(r'^#([0-9a-f]{6}$)', data)
    if match is not None:
        valid = True
    return valid


def eclCheck(data):  # eye color check
    valid = False
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    reqEcls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for ecl in reqEcls:
        if data == ecl:
            valid = True
            break
    return valid


def pidCheck(data):  # passport ID check
    valid = False
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # What do the ^ and $ in this regex do? They reduced the valid count by 1!
    if re.match(r'^\d{9}$', data) is not None:
        valid = True
    return valid


passports = findData(readInput('day4-input.txt'))
validPassports = checkValidity(passports)
