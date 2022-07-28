# n = int(input())
# ranked = set(input().split(" "))
# m = int(input())
# player = input().split(" ")

n = 7
ranked = sorted(set("100 100 50 40 40 20 10".split(" ")), key = lambda x:int(x))
m = 4
player = "5 25 50 120".split(" ")

print(ranked)

index = 0
for x in range(m):
    for y in range(index, len(ranked)):
        if int(player[x]) < int(ranked[y]):
            print(len(ranked) + 1 - y)
            index = y
            break
        elif int(player[x]) == int(ranked[y]):
            print(len(ranked) - y)
            index = y
            break
        elif y+1 == len(ranked):
            print(len(ranked) - y)

