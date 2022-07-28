import itertools
k, a = input(), itertools.groupby(sorted(input().split()))
for x, y in a:
    if len(list(y)) != int(k):
        print(x)
        break