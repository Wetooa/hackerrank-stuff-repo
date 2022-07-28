def possible(array, k):
    for a in range(len(array)-1):
        for b in range(a+1, len(array)):
            if array[a] + array[b] % k != 0:
                return False
    print("yes")
    return True


n, k = input().split(" ")
main_array = input().split(" ")

for x in range(int(n), 1, -1):
    for y in range(int(n)):
        if int(n) - y >= x:
            current = []
            for z in range(y, y+x):
                current.append(int(main_array[z]))
            print(current)
            if possible(current, int(k)):
                print(len(current))
                quit()
        else:
            break