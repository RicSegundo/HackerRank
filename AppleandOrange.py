
s, t = 7, 11
a, b = 5, 15
m, n = 3, 2
apple_list = [-2, 2, 1]
orange_list = [5, -6]


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [x+a for x in apples]
    oranges = [x+b for x in oranges]

    result = [sum(s <= i <= t for i in apples), sum(s <= j <= t for j in oranges)]

    print(*result, sep='\n')


countApplesAndOranges(s, t, a, b, apple_list, orange_list)

