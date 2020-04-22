

n = 100000
p = 2
astronaut_pairs = [[0, 1], [2, 3], [0, 4], [5, 6], [4, 5]]
# astronaut_pairs = [[1, 2], [3, 4]]


def make_equiv_classes(pairs):
    groups = {}
    for (x, y) in pairs:
        xset = groups.get(x, set([x]))
        yset = groups.get(y, set([y]))
        jset = xset | yset
        for z in jset:
            groups[z] = jset
    return [item for item in set(map(tuple, groups.values()))]


def combinations(astr, k):
    if 0 <= k <= astr:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, astr - k) + 1):
            ntok *= astr
            ktok *= t
            astr -= 1
        return ntok // ktok
    else:
        return 0


def journeyToMoon(n, astronaut):
    all_possible_pairs = combinations(n, 2)
    country_pairs = sum(combinations(len(country), 2) for country in make_equiv_classes(astronaut))
    return all_possible_pairs - country_pairs


if __name__ == '__main__':
    # np = input().split()
    # n = int(np[0])
    # p = int(np[1])
    # astronaut = []
    # for _ in range(p):
    #     astronaut.append(list(map(int, input().rstrip().split())))

    print(journeyToMoon(n, astronaut_pairs))

