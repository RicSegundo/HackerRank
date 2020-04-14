
from itertools import combinations

n = 4
car = ['a', 'a', 'c', 'd']
k = 2


def iterables(car, k):
    print(len([element.count('a') for element in list(combinations(car, k)) if element.count('a') > 0]) / len(list(combinations(car, k))))


if __name__ == '__main__':
    # string, k = input(), int(input())
    iterables(car, k)


