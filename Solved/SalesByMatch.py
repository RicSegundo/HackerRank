#!/bin/python3

import os
import collections

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    freq = collections.Counter(ar)
    occur = freq.values()
    return sum([oc//2 for oc in occur])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
