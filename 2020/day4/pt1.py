#!/usr/bin/env python3

import sys
import pprint

pprinter = pprint.PrettyPrinter(indent=4)
rawInput = sys.stdin.read()

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
validpassports = list(passports)
print("validpassports:")
pprinter.pprint(validpassports)
for passport in passports:
    print(f"Checking {passport}")
    for field in requiredfields:
        if field not in passport:
            print(f"    {field}: missing")
            validpassports.remove(passport)
            break
        else:
            print(f"    {field}: found")

print("---> SUMMARY")
print(f"Valid passports: {len(validpassports)}")