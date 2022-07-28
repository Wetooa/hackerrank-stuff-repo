n, k, q = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
for x in range(k):
    array.insert(0, array.pop())
for _ in range(q):
    print(array[int(input().strip())])