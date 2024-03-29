#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valleys = 0
    level = 0
    valley = False
    for direction in path:
        if direction == 'U':
            level += 1
            if valley and level >= 0:
                valley = False
        else:
            level -= 1
            if valley == False and level == -1:
                valley = True
                valleys += 1
    
    return valleys
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
