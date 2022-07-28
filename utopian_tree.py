n = int(input().strip())
for _ in range(n):
    height = 1
    for x in range(int(input().strip())):
        if x % 2 == 0:
            height *= 2
        else:
            height += 1
    print(height)