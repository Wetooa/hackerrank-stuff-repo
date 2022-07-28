n = int(input().strip())
people = 5
likes = 0
for x in range(n):
    likes += people // 2
    people = people // 2 * 3
print(likes)