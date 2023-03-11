n = 5
m = 4

matr = [[0 for col in range(n)] for row in range(m)]
r, c, vr, vc = 0, 0, 0, 1

for i in range(1, n * m + 1):
    if (c > n - 1) or (c < 0) or (r > m - 1) or (r < 0) or (matr[r][c] > 0):
        r -= vr
        c -= vc
        vr, vc = vc, -vr
        r += vr
        c += vc

    matr[r][c] = i
    r += vr
    c += vc

for p in matr:
    print(*p, sep="\t")

