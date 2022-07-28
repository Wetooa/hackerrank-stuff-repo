n = int(input().strip())
array = list(map(int, input().strip().split()))
dict = {}
count = 0
for x in array:
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] += 1
        if dict[x] % 2 == 0:
            count += 1
print(count)