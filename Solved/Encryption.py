

def encryption(s):
    s = [i for i in s.replace(" ", "")]

    columns = int(len(s) ** 0.5) if (len(s) ** 0.5).is_integer() else int(len(s) ** 0.5) + 1
    rows = int(len(s) ** 0.5)
    # Check columns x rows >= then L condition
    if (columns * rows) < len(s):
        rows += 1

    final = [[] for i in range(columns)]

    for index, char in enumerate(s):
        final[(index % columns)].append(char)

    final = [''.join(i) for i in final]

    print(*final, sep=' ')


if __name__ == '__main__':
    s_0 = 'chillout'
    encryption(s_0)



