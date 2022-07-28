def check(array, dict, sorted_arrayz):
    count = 0
    print(array)
    print(dict)
    print(sorted_arrayz)
    for x in range(len(array)):
        if array[x] != sorted_arrayz[x]:
            count += 1
            correct_index = dict[sorted_arrayz[x]]
            array[x], array[correct_index] = array[correct_index], array[x]
            dict[array[correct_index]] = dict[sorted_arrayz[x]]
    print(array)
    print(count)
    return count


n = int(input().strip())
array1 = list(map(int, input().strip().split()))
array2 = array1

dict_array1 = dict([[array1[x], x] for x in range(len(array1))])
dict_array2 = dict([[array2[x], x] for x in range(len(array2))])

sorted_array = sorted(array1)
reversed_sorted_array = sorted(array2, reverse=True)

print(min(check(array1, dict_array1, reversed_sorted_array), check(array2, dict_array2, sorted_array)))