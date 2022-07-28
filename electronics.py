def pick():
    possible = []
    for x in range(n - 1):
        cost = 0
        for y in range(n+1, m):
            cost = keyboard[x] + usb[y]
            if cost <= b:
                possible.append(cost)
    if len(possible) != 0:
        return sorted(possible, reverse=True)[0]
    return -1

b, n, m = map(int, input().strip().split())
keyboard = sorted(map(int, input().strip().split()))
usb = sorted(map(int, input().strip().split()))

print(pick())