
from itertools import product

# K, M = map(int,input().split())
K, M = 3, 1000

# N = (list(map(int, input().split()))[1:] for _ in range(K))
N = [[5, 4], [7, 8, 9], [7, 8, 9, 10]]

results = map(lambda x: sum(i**2 for i in x) % M, product(*N))

print(max(results))
# print(results)

