
string = 'AABCAAADA'
k = 3


def merge_the_tools(string, k):
    print(*["".join(dict.fromkeys(string[i:i+k])) for i in range(0, len(string), k)], sep='\n')


if __name__ == '__main__':
    # string, k = input(), int(input())
    merge_the_tools(string, k)

