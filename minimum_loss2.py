n = int(input().strip())
array = list(map(int, input().strip().split()))
dict = {k: v for v, k in enumerate(array)}
array = sorted(array, reverse=True)
lowest = array[0]
for x in range(n-1):
    if dict[array[x]] < dict[array[x + 1]] and array[x] - array[x + 1] < lowest and array[x] - array[x + 1] > 0:
        lowest = array[x] - array[x + 1]
print(lowest)