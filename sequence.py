n = int(input().strip())
array = list(map(int, input().strip().split()))
for x in range(1, n + 1):
    print(array.index(array.index(x) + 1) + 1)