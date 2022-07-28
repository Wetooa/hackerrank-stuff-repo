import math


n = int(input().strip())
squares = []
square_count = 1
for _ in range(n):
    s, e = map(int, input().strip().split())
    count = 0
    while len(squares) == 0 or squares[-1] < e:
        squares.append(square_count**2)
        square_count += 1
    for x in range(len(squares)):
        if squares[x] in range(s, e+1):
            count += 1
    print(count)
