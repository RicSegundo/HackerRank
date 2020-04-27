import math

n = 2
a = 100
b = 1000

print(math.ceil((a ** 0.5)))
print(math.floor((b ** 0.5)))


def squares(a, b):
    square_roots = (math.floor((b ** 0.5)) - math.ceil((a ** 0.5))) + 1
    print(square_roots)


if __name__ == '__main__':
    squares(a, b)

