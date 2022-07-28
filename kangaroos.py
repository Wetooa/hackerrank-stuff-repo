stats = [int(x) for x in input().split(" ")]

if stats[0] < stats[2]:
    stats[2] -= stats[0]
    stats[0] = 0
else:
    stats[0] -= stats[2]
    stats[2] = 0

run = True
while run:
    stats[0] += stats[1]
    stats[2] += stats[3]
    if stats[0] == stats[2]:
        print("YES")
        run = False
    if (stats[0] > stats[2] and stats[1] > stats[3]) or (stats[0] < stats[2] and stats[1] < stats[3]) or stats[1] == stats[3]:
        print("NO")
        run = False