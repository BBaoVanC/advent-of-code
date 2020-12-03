#!/usr/bin/env python3

import sys
import math

rawInput = sys.stdin.readlines()

# Remove newlines from the end of everything
strippedInput = []
for line in rawInput:
    strippedInput.append(line.strip())


# Repeat to the right enough times
wantcols = 3 * len(strippedInput) + 1
multcols = math.ceil(wantcols / len(strippedInput[0])) + 1

newInput = []
for line in strippedInput:
    newInput.append(line * multcols)
# -+-> newInput is now strippedInput, but repeated horizontally enough times

if len(sys.argv) > 1:
    if sys.argv[1] == "genmap":
        print("\n".join(newInput))
        exit(0)

trees = 0
for i in range(1, len(newInput)):
    if newInput[i][i*3] == "#":
        trees += 1
        print(f"Hit tree at {i+1},{i*3+1}")
    else:
        print(f"No tree at  {i+1},{i*3+1}")

print()
print(f"---> SUMMARY")
print(f"Trees hit:  {trees}")
