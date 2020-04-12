
line_0 = [2081, 8403, 9107, 8400]

x1 = int(line_0[0])
v1 = int(line_0[1])
x2 = int(line_0[2])
v2 = int(line_0[3])


def kangaroo(x1, v1, x2, v2):

    if v1 > v2 and ((x2-x1)/(v1-v2)).is_integer():
        result = 'YES'
    else:
        result = 'NO'

    return result


print(kangaroo(x1, v1, x2, v2))

