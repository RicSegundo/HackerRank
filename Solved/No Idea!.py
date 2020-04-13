
n = 3
m = 2
array = [1, 5, 3]
like = [3, 1]
dislike = [5, 7]


def happiness_counter(array, like, dislike):
    happ_counter = 0
    for elem in array:
        if elem in like:
            happ_counter += 1
        if elem in dislike:
            happ_counter -= 1

    return happ_counter


print(happiness_counter(array, like, dislike))


"""
Final solution, due to the timeout of the previous one for very large arrays
The trick is to transform the like and dislike into sets and not lists

n, m = map(int,input().split())
array = input().split(' ')
like = set(input().split(' '))
dislike = set(input().split(' '))

print(sum((i in like) - (i in dislike) for i in array))
"""
