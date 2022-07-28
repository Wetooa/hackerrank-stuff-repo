n = int(input().strip())
array = input().strip()
level = 0
valleys = 0
for x in range(n):
    if array[x] == "D":
        level -= 1
    else:
        level += 1

    if level == 0 and array[x] == "U":
        valleys += 1
print(valleys)