p, d, m, s = map(int, input().strip().split())
count = 0
while s >= p:
    count += 1
    s -= p
    if p > m:
        p -= d
    if p <= m:
        p = m
print(count)