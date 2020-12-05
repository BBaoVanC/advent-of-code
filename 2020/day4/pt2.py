#!/usr/bin/env python3

import sys
import re
import pprint

pprinter = pprint.PrettyPrinter(indent=4)
rawInput = sys.stdin.read()


def checkRange(num, min, max):
    try:
        if min <= int(num) <= max:
            return True
        else:
            return False
    except ValueError:
        return False


def checkHgt(rawhgt):
    try:
        hgt = int(rawhgt[:-2])
    except ValueError:
        return False
    if rawhgt.endswith("cm"):
        if not 150 <= hgt <= 193:
            return False
        else:
            return True
    elif rawhgt.endswith("in"):
        if not 59 <= hgt <= 76:
            return False
        else:
            return True
    else:
        return False


# Split by blank lines (split into a list of separate passport strings)
splitRawInput = rawInput.split("\n\n")

# Convert to a two-dimensional table
tableInput = [s.split() for s in splitRawInput]

# Convert to a list of dictionaries
passports = []
for passport in tableInput:
    dictpass = {}
    for pair in passport:
        splitpair = pair.split(":")
        dictpass[splitpair[0]] = splitpair[1]

    passports.append(dictpass)

requiredfields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    #"cid",
]
valideyecolors = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth",
]
validpassports = list(passports)
print("validpassports:")
pprinter.pprint(validpassports)
for passport in passports:
    cont = True
    print(f"Checking {passport}")
    for field in requiredfields:
        if field not in passport:
            print(f"    {field}: missing")
            validpassports.remove(passport)
            cont = False
            break
    if cont:
        if not checkRange(passport["byr"], 1920, 2002):
            print(f"Failed byr: {passport}")
            validpassports.remove(passport)
            continue
        elif not checkRange(passport["iyr"], 2010, 2020):
            print(f"Failed iyr: {passport}")
            validpassports.remove(passport)
            continue
        elif not checkRange(passport["eyr"], 2020, 2030):
            print(f"Failed eyr: {passport}")
            validpassports.remove(passport)
            continue
        elif not checkHgt(passport["hgt"]):
            print(f"Failed hgt: {passport}")
            validpassports.remove(passport)
            continue
        elif not re.search("#[0-9a-f]{6}", passport["hcl"]):
            print(f"Failed hcl: {passport}")
            validpassports.remove(passport)
            continue
        elif not passport["ecl"] in valideyecolors:
            print(f"Failed ecl: {passport}")
            validpassports.remove(passport)
            continue
        elif not re.search("^[0-9]{9}$", passport["pid"]):
            print(f"Failed pid: {passport}")
            validpassports.remove(passport)
            continue

print("---> SUMMARY")
print(f"Valid passports: {len(validpassports)}")