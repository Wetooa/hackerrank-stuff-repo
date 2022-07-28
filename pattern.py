n = int(input())
for _ in range(n):
    big_rows, big_length = input().split(" ")
    big_array = []
    for x in range(int(big_rows)):
        big_array.append(input())

    small_rows, small_length = input().split(" ")
    small_array = []
    for x in range(int(small_rows)):
        small_array.append(input())
    
    answer = False
    for x in range(int(big_rows)):
        if small_array[0] in big_array[x] and int(big_rows) - x >= int(small_rows):
            for z in range(big_array[x].index(small_array[0]), int(big_length)):
                if small_array[0] == big_array[x][z:z+int(small_length)]:
                    small_iterator = 1
                    for y in range(x+1, x+1+int(small_rows)):
                        if small_array[small_iterator] not in big_array[y][z:z+int(small_length)]:
                            break
                        elif small_iterator + 1 == int(small_rows):
                            answer = True
                            break
                        small_iterator += 1
    if answer:
        print("YES")
    else:
        print("NO")