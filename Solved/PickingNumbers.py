from collections import Counter

a = list(map(int, '4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97'.rstrip().split()))

def pickingNumbers(a):
    freq = dict(sorted(Counter(a).items()))

    if len(freq.keys()) == 1:
        return freq.get(a[0])

    else:
        max_val = 0
        previous_key = None
        for key in freq.keys():
            if key - 1 == previous_key:
                sum_consecutive = freq.get(key) + freq.get(previous_key)
                if sum_consecutive > max_val:
                    max_val = sum_consecutive
            previous_key = key

        return max_val if max_val > max(freq.values()) else max(freq.values())


print(pickingNumbers(a))

