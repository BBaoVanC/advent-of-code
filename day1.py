#!/usr/bin/env

import sys

rawInput = sys.stdin.readlines()

strnums = []
for line in rawInput:
    strnums.append(line.strip())

# convert to integers
nums = []
for num in strnums:
    nums.append(int(num))

for n1 in nums:
    for n2 in nums:
        if n1 + n2 == 2020:
            print(f"{n1} + {n2} = 2020")
