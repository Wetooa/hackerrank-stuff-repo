n, k = map(int, input().strip().split())
array = sorted(list(map(int, input().strip().split())), reverse=True)
set = set(array)
count = 0
for x in range(n - 1):
    if array[x] - k in set:
        count += 1
print(count)