
# heights = list(map(int, input().split()))
heights = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
# word = input().split()
word = ['z', 'a', 'b', 'a']

values = {chr(i + 97): heights[i] for i in range(ord("a") - 97, ord("a") - 97 + 26)}

print(max(values[j] for j in word) * len(word))

