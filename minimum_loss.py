n = int(input().strip())
array = list(map(int, input().strip().split()))
lowest = max(array)
for x in range(n):
    for y in range(x + 1, n):
        price_diff = array[x] - array[y]
        if price_diff > 0 and price_diff < lowest:
            lowest = price_diff
print(lowest)