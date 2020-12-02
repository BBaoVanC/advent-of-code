#!/usr/bin/env

import sys

rawInput = sys.stdin.readlines()

input = []
for line in rawInput:
    input.append(line.strip())

halfpoint = int(len(input) / 2)
i1 = input[:halfpoint]
i2 = input[halfpoint:]

for n1 in i1:
    for n2 in i2:
        if n1 + n2 == 2020:
            print(f"{n1} + {n2} = 2020")
