#!/bin/python3

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.pop(k)
    Ann_value = sum(bill)/2
    if Ann_value == b:
        print('Bon Appetit')
    else:
        print(int(b - Ann_value))

if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
