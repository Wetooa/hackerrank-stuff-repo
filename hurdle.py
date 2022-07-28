n, k = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
if max(array) - k > 0:
    print(max(array) - k)
else:
    print(0)