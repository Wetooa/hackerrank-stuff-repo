n, d = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
count = 0
for x in range(n):
    if d + array[x] in array and d * 2 + array[x] in array:
        count += 1
print(count)