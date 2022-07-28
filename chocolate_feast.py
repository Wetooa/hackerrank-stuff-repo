q = int(input().strip())
for _ in range(q):
    n, c, m = map(int, input().strip().split())
    bars = n / c
    wrappers = bars
    while wrappers >= m:
        new_bars = wrappers // m
        bars += new_bars
        wrappers -= new_bars * m - new_bars
    print(int(bars))
