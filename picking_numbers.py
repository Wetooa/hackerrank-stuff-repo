import itertools
n = int(input().strip())
array = itertools.groupby(sorted(list(map(int, input().strip().split()))))
first_num = 0
second_num = 0
current_largest = 0
x_before = 0
for x, y in array:
    second_num = first_num
    first_num = len(list(y))
    if current_largest == 0:
        current_largest = first_num
    if first_num + second_num > current_largest and x_before != 0 and abs(x - x_before) <= 1:
        current_largest = second_num + first_num
    if first_num > current_largest:
        current_largest = first_num
    x_before = int(x)
print(current_largest)