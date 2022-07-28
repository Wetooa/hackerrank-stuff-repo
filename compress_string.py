import itertools # use this for stuff like this
a = input()
x = itertools.groupby(a)
print(list(x))
for k,g in x:
    print(f"({len(list(g))}, {k})", end = " ")