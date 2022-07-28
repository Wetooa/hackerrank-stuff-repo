n, k = map(int, input().strip().split(" "))
numbers = list(map(int, input().strip().split(" ")))

remainders = []
for x in range(n):
    for y in range(n):
        if x != y and numbers[x] + numbers[y] % k != 0:
            remainders.append(numbers[x] % k)
            break

count = 0
counter = 0
for x in range(len(remainders)):
    if k - remainders[x] in remainders:
        if remainders.count(remainders[x]) > remainders.count(k - remainders[x]):
            count += 1
    else:
        count += 1
if k % 2 == 0:
    count += 1

print(count)