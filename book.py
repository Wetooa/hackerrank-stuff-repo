import math


n = int(input().strip())
p = int(input().strip())

if n % 2 == 0:
    n += 1
if p > n / 2:
    p = n - p

count = math.ceil((p - 1) / 2)

print(count)