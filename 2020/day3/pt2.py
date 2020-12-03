#!/usr/bin/env python3

import sys
import math

rawInput = sys.stdin.readlines()

# Remove newlines from the end of everything
strippedInput = []
for line in rawInput:
    strippedInput.append(line.strip())


# Repeat to the right enough times
wantcols = 7 * len(strippedInput) + 1
multcols = math.ceil(wantcols / len(strippedInput[0])) + 1

newInput = []
for line in strippedInput:
    newInput.append(line * multcols)
# -+-> newInput is now strippedInput, but repeated horizontally enough times

if len(sys.argv) > 1:
    if sys.argv[1] == "genmap":
        print("\n".join(newInput))
        exit(0)

trees1_1 = 0
for i in range(1, len(newInput)):
    if newInput[i][i] == "#":
        trees1_1 += 1

trees1_3 = 0
for i in range(1, len(newInput)):
    if newInput[i][i*3] == "#":
        trees1_3 += 1

trees1_5 = 0
for i in range(1, len(newInput)):
    if newInput[i][i*5] == "#":
        trees1_5 += 1

trees1_7 = 0
for i in range(1, len(newInput)):
    if newInput[i][i*7] == "#":
        trees1_7 += 1

trees2_1 = 0
for i in range(1, len(newInput)):
    try:
        if newInput[i*2][i] == "#":
            trees2_1 += 1
    except IndexError:
        pass

print()
print(f"---> SUMMARY")
print(f"down 1, right 1:  {trees1_1}")
print(f"down 1, right 3:  {trees1_3}")
print(f"down 1, right 5:  {trees1_5}")
print(f"down 1, right 7:  {trees1_7}")
print(f"down 2, right 1:  {trees2_1}")
print(f"---> MULTIPLIED TOGETHER ")
product = trees1_1 * trees1_3 * trees1_5 * trees1_7 * trees2_1
print(product)
