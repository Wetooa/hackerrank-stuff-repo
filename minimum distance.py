n = int(input().strip())
array = list(map(int, input().strip().split()))
minimum = len(array)
for x in range(n - 1):
    for y in range(x + 1, n):
        if array[x] == array[y] and abs(x - y) < minimum:
            minimum = abs(x - y)
if minimum == len(array):
    print(-1)
else:
    print(minimum)