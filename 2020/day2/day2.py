#!/usr/bin/env python3

import sys

rawInput = sys.stdin.readlines()

valid = 0
invalid = 0
for check in rawInput:
    print()
    split1tuple = check.partition(":")  # ("1-3 a", ":", "abcde")
    split1 = list(split1tuple)  # convert to list
    split1[-1] = split1[-1].strip()  # remove newline from last item

    split2tuple = split1[0].partition("-")  # ("1", "-", "3 a")
    split2str = [split2tuple[0], split2tuple[2][:-2], split2tuple[2][-1]]  # ["1", "3", "a"]
    split2 = [int(split2str[0]), int(split2str[1]), split2str[2]]  # [1, 3, "a"]

    ccount = 0
    for char in split1[2]:
        if char == split2[2]:
            ccount += 1
    print(f"There are {ccount} {split2[2]}'s")

    if split2[0] <= ccount <= split2[1]:
        valid += 1
        print(f"Valid:      {check.strip()}")
    else:
        invalid += 1
        print(f"Invalid:    {check.strip()}")

print()
print("---> SUMMARY")
print(f"Valid:      {valid}")
print(f"Invalid:    {invalid}")
