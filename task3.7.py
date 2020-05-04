s = input('enter: ')
def hackerrankInString(s):
    key_string = 'hackerrank'
    a = 0
    for i in s:
        if i == key_string[a]:
            a += 1
        if a == len(key_string):
            break
    if a == len(key_string):
        return 'YES'
    else: 
        return 'NO'
print(hackerrankInString(s))

"""
    #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    key_string = 'hackerrank'
    a = 0
    for i in s:
        if i == key_string[a]:
            a += 1
        if a == len(key_string):
            break
             
    if a == len(key_string):
        return 'YES'
    else: 
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
"""