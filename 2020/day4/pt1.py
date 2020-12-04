#!/usr/bin/env python3

import sys

rawInput = sys.stdin.read()

splitRawInput = rawInput.split("\n\n")

tableInput = [s.split("\n") for s in splitRawInput]
print(tableInput)
