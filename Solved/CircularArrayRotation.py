

n, k, q = 3, 4, 3
arr = [1, 2, 3]
queries = [0, 1, 2]


def circularArrayRotation(arr, k, queries):
    return [arr[(i-k) % n] for i in queries]


if __name__ == '__main__':
    print(circularArrayRotation(arr, k, queries))

