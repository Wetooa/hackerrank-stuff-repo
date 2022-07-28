t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().strip().split())
    array = list(map(int, input().strip().split()))
    count = 0
    for x in range(n):
        if array[x] <= 0:
            count += 1
        if count > k:
            break
    if count >= k:
        print("NO")
    else:
        print("YES")
    