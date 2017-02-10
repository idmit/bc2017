import sys

rna = sys.stdin.readline().rstrip()
n = len(rna)

m = [[0 for _ in range(n)] for _ in range(n)]


def comp(sym):
    return comp.d[sym]


comp.d = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}

for s in range(1, n):
    for i in range(n - s):
        j = i + s

        ins = [m[i][k] + m[k + 1][j] for k in range(i + 1, j - 1)]
        in_max = max(ins) if ins else 0

        opts = [m[i + 1][j], m[i][j - 1], in_max]
        if rna[i] == comp(rna[j]):
            opts.append(m[i + 1][j - 1] + 1)

        m[i][j] = max(opts)

if m[0][n - 1] == n // 2:
    if n % 2:
        print("almost perfect")
    else:
        print("perfect")
else:
    print("imperfect")
