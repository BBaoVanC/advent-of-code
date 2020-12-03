#!/usr/bin/env python3

import sys

rawInput = sys.stdin.readlines()

check = rawInput[0]
split1tuple = check.partition(":")  # ("1-3 a", ":", "abcde")
split1 = list(split1tuple)  # convert to list
split1[-1] = split1[-1].strip();  # remove newline from last item

split2tuple = split1[0].partition("-")  # ("1", "-", "3 a")
split2 = [split2tuple[0], split2tuple[2][0], split2tuple[2][-1]]  # ["1", "3", "a"]

if true:
    print("It works!")
