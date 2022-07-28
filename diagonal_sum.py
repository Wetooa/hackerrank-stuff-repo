n = int(input())
absolute_sum = 0
for x in range(n):
    current = input().split(" ")
    for y in range(n):
        if y == x:
            absolute_sum += int(current[y])
        if y == n - 1- x:
            absolute_sum -= int(current[y])

print(abs(absolute_sum))
