n = int(input())
scores = [int(x) for x in input().split(" ")]

lower = 0
higher = 0
minimum = 0
maximum = 0
for x in range(len(scores)):
    if x == 0:
        maximum = scores[x]
        minimum = scores[x]
    if scores[x] > maximum:
        maximum = scores[x]
        higher += 1
    elif scores[x] < minimum:
        minimum = scores[x]
        lower += 1

print(f"{higher} {lower}")