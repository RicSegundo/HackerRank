

s = 'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv'
t = 'bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv'
k = 100


def appendAndDelete(s, t, k):
    if len(t) > len(s):
        if ((len(t) - len(s)) % 2) == (k % 2):
            return 'Yes'
        else:
            return 'No'

    else:
        counter = -1
        for a, b in zip(s, t):
            counter += 1
            if a != b:
                if (len(s)-counter) + (len(t)-counter) > k:
                    return 'No'
                    break
                else:
                    return 'Yes'
                    break

        if len(t)-1 == counter:
            if len(s) - 1 - counter > k:
                return 'No'
            else:
                return 'Yes'

        return 'Yes'


if __name__ == '__main__':
    print(appendAndDelete(s, t, k))

