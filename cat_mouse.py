n = int(input().strip())

for x in range(n):
    array = list(map(int, input().strip().split()))
    if abs(array[2] - array[0]) > abs(array[2] - array[1]):
        print("Cat B")
    elif abs(array[2] - array[0]) < abs(array[2] - array[1]):
        print("Cat A")
    else:
        print("Mouse C")