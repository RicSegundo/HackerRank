from itertools import product

keyboards = [4]
drives = [5]
b = 5

def getMoneySpent(keyboards, drives, b):
    possible_purchases = [sum(x) for x in list(product(keyboards, drives)) if sum(x) <= b]
    return max(possible_purchases) if possible_purchases else -1

print(getMoneySpent(keyboards, drives, b))


# Official solution submitted

"""
#!/bin/python3

import os
import sys
from itertools import product

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    possible_purchases = [sum(x) for x in list(product(keyboards, drives)) if sum(x) <= b]
    return max(possible_purchases) if possible_purchases else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
"""