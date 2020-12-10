#!/usr/bin/env python3

import sys
import logging

logging.basicConfig(level=logging.INFO)
rawInput = sys.stdin.readlines()


# Strip newlines
strippedInput = []
for line in rawInput:
    strippedInput.append(line.strip())


def splitArgs(instruction):
    i, a = instruction.split(" ")
    return (i, int(a))


def nop(args):
    global curLn
    curLn += 1


def acc(args):
    global curLn
    global accumulator
    curLn += 1
    accumulator += args


def jmp(args):
    global curLn
    curLn += args


insMap = {
    "nop": nop,
    "acc": acc,
    "jmp": jmp,
}


doneLines = []
accumulator = 0
done = False
curLn = 0
while True:
    if curLn in doneLines:
        print(f"accumulator = {accumulator}")
        break
    doneLines.append(curLn)
    ins, arg = splitArgs(strippedInput[curLn])
    insMap[ins](arg)
