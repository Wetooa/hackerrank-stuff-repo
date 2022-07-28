import itertools
l = itertools.groupby(sorted(input().split()))
print(l)
a = []
for x, y in l:
    a.append((x, len(list(y))))
print(a)

# OP VERSION DOWN BELOW

print([(x, len(list(y))) for x, y in (itertools.groupby(sorted(input().split())))])