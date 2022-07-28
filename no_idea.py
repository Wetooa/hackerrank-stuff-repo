lengths = input().split()
array1 = input().split()
a = set(input().split())
b = set(input().split())

happiness = 0
for i in array1:
    if i in a:
        happiness += 1
    elif i in b:
        happiness -= 1

print(happiness)