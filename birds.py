import itertools
n = int(input().strip())
array = itertools.groupby(sorted(list(map(int, input().strip().split()))))
dict = {}
for x, y in array:
    if x not in dict:
        dict[x] = len(list(y))
    else:
        dict[x] += 1
print(list(sorted(dict.items(), key = lambda x:x[1], reverse=True))[0][0])

