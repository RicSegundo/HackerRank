

n = 11
birds = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]


def migratoryBirds(birds):
    count = [0]*6
    for t in arr:
        count[t] += 1
    print(count.index(max(count)))


if __name__ == '__main__':
    # arr_count = int(input().strip())
    # birds = list(map(int, input().rstrip().split()))

    migratoryBirds(birds)

