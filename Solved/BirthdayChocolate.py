

n = 5
choc = [1, 2, 1, 3, 2]
d, m = 3, 2


def birthday(choc, d, m):

    return sum(element == d for element in [sum(choc[i:i+m]) for i in range(len(choc)) if i+m <= len(choc)])


print(birthday(choc, d, m))

