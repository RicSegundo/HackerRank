import time

start = time.time()
# s = 'aaabccddd'
s = 'zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'


def superReducedString(s):
    test = list(s)
    index = 0
    while index + 1 < len(test):
        if index < len(test) and test[index] == test[index+1]:
            del test[index+1]
            del test[index]
            index = 0
            # print(test)
        else:
            index += 1
    if len(test) == 0:
        print('Empty String')
    else:
        print(*test, sep='')


if __name__ == '__main__':
    superReducedString(s)

print(time.time() - start)

