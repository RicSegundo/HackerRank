#!/bin/python3

import os

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    return min([int((p-1)/2) + ((p-1) % 2 > 0), (n// 2) - (p // 2)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
