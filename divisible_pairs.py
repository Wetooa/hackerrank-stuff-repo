n, k = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
count = 0
for x in range(n-1):
    for y in range(x+1, n):
        if x != y and (array[x] + array[y]) % k == 0:
            count += 1
print(count)