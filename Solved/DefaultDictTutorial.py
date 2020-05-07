from collections import defaultdict

dictionary = defaultdict(list)

n, m = map(int, input().split())

for i in range(1, n+1):
    dictionary[input()].append(i)

for i in range(m):
    B = input()
    if B in dictionary:
        print(*dictionary[B], sep=' ')
    else:
        print(-1)