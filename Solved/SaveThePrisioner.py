

n = 3
m = 7
s = 3

def saveThePrisoner(n, m, s):
    return (n if (((s-1) + (m % n)) % n) == 0 else ((s-1) + (m % n)) % n)


print(saveThePrisoner(n, m, s))

