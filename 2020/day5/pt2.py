#!/usr/bin/env python3

import sys
import logging

logging.basicConfig(level=logging.WARN)
rawInput = sys.stdin.readlines()

# Remove newlines
passports = []
for line in rawInput:
    passports.append(line.strip())


# For each passport
sids = {}
for passport in passports:
    # Split up into the first 7 chars and the rest
    rowstr = passport[:7]
    colstr = passport[7:]
    pRows = list(range(0, 128))  # 0-127
    for c in rowstr:
        logging.debug(f"rowstr is {rowstr}")
        pivot = int(len(pRows) / 2)
        logging.debug(f"pivot is {pivot}")
        if c == "F":
            logging.debug(f"    Splitting for the first half")
            pRows = pRows[:pivot]
        elif c == "B":
            logging.debug(f"    Splitting for the last half")
            pRows = pRows[pivot:]
        else:
            raise ValueError("Neither F or B")
        logging.debug(f"    pRows is now {pRows}")

    assert len(pRows) == 1, f"len(pRows) = {len(pRows)}"
    row = pRows[0]

    pCols = list(range(0, 8))  # 0-7
    for c in colstr:
        logging.debug(f"colstr is {colstr}")
        pivot = int(len(pCols) / 2)
        logging.debug(f"pivot is {pivot}")
        if c == "L":
            logging.debug(f"    Splitting for the first half")
            pCols = pCols[:pivot]
        elif c == "R":
            logging.debug(f"    Splitting for the last half")
            pCols = pCols[pivot:]
        else:
            raise ValueError("Neither F or B")
        logging.debug(f"    pCols is now {pCols}")
    
    assert len(pCols) == 1, f"len(pCols) = {len(pCols)}"
    col = pCols[0]
    sid = row * 8 + col
    logging.info(f"Row {row}, Col {col}, SID {sid}")
    sids[sid] = [row, col]

pSIDs = dict(sids)  # SIDs that could be mine

for seat in sids:
    print(f"Seat {seat}, location {pSIDs[seat]}")
    if pSIDs[seat][0] == 0 or pSIDs[seat][0] == 127:
        print(f"Removing {pSIDs[seat]} with SID {seat}")
        pSIDs.pop(seat)

print(f"Length: {len(pSIDs)}")
