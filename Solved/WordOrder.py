

n = 4
words = ['bcdef', 'abcdefg', 'bcde', 'bcdef']


def word_order(string):
    print(*[string.count(x) for x in dict.fromkeys(string).keys()], sep=' ')


if __name__ == '__main__':
    # n = int(input())
    # words = []
    # for _ in range(n):
    #    words.append(str(input()))
    word_order(words)

