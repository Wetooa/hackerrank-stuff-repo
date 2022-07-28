n = int(input().strip())
people = list(map(int, input().strip().split()))
count = 0
for x in range(len(people)):
    if people[x] % 2 != 0:
        people[x] += 1
        try:
            next_person = people[x + 1]
        except:
            people[x - 1] += 1
            if people[x - 1] % 2 != 0:
                print("NO")
                quit()
        else:
            people[x + 1] += 1
        count += 2
print(count)