
s1 = 'cde'
s2 = 'abc'

s1 = 'bugexikjevtubidpulaelsbcqlupwetzyzdvjphn'
s2 = 'lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk'


def makingAnagrams(s1, s2):
    all_chrs = set(s1 + s2)
    dict_1 = {i: s1.count(i) for i in all_chrs}
    dict_2 = {i: s2.count(i) for i in all_chrs}
    return sum(abs(dict_1[ch] - dict_2[ch]) for ch in all_chrs)


if __name__ == '__main__':
    # s1 = input()
    # s2 = input()
    print(makingAnagrams(s1, s2))

