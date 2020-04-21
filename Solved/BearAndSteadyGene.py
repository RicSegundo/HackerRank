

def balanced(n, dic):
        bal = True
        for k, v in dic.items():
                if v > n:
                        bal = False
                        break
        return bal


# Complete the steadyGene function below.
def steadyGene(gene):
    n = len(gene)
    g_n = n/4
    gene_freq = {i: gene.count(i) for i in nucleotides}

    min_ans = 10**9
    right = left = 0
    while right < n and left < n:
        if not balanced(g_n, gene_freq):
            gene_freq[gene[right]] -= 1
            right += 1
        else:
            min_ans = min(min_ans,  right - left)
            gene_freq[gene[left]] += 1
            left += 1

    return min_ans


if __name__ == '__main__':
    # n = int(input())
    n = 8
    # gene = input()
    gene = 'GAAATAAA'

    nucleotides = ['A', 'C', 'G', 'T']

    print(steadyGene(gene))

