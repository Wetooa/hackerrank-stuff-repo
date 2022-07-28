from itertools import combinations
s1 = list(input().strip())
s2 = list(input().strip())

common = set(set(s1).intersection(set(s2)))
a1, a2 = [], []
for x in range(len(s1)):
    if s1[x] in common:
        a1.append(s1[x])
    if s2[x] in common:
        a2.append(s2[x])

print(common)
print(a1)
print(a2)

for x in range(len(min(a1, a2)), 0, -1):
    b1 = []
    b2 = []
    for y in range(x):
        if len(a1) - a1.index(a1[y]) >= x and len(a1) - a2.index(a1[y]) >= x:
            b1.append(a1[])
    # comb1 = set(combinations(a1, x))
    # comb2 = set(combinations(a2, x))
    # for y in comb1:
    #     if y in comb2:
    #         print(len(y))
    #         quit()


print(0)

#ahhh shit man ka lisod ani oi hahahahah