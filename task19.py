#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    n_valleys = 0
    for i in range(n):
        if s[i] == 'U':
            height += 1
            if height == 0:
                n_valleys += 1
        else:
            height -= 1
    return n_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
