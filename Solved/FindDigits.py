#!/bin/python3

import os

# Complete the findDigits function below.
def findDigits(n):
    res = 0
    int_list = [int(d) for d in str(n)]
    for number in int_list:
        if number != 0 and n % number == 0:
            res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
