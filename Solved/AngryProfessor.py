
k = 3
a = [-1, -3, 4, 2]


def angryProfessor(k, a):
    if len([i for i in a if i <= 0]) >= k:
        return 'NO'
    else:
        return 'YES'


print(angryProfessor(k, a))

