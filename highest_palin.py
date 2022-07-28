n , k = map(int, input().strip().split())
s = list(map(int, [x for x in input().strip()]))
index = []
for x in range(int(n//2)):
    if s[x] != s[(x + 1) * -1]:
        index.append(x)
if len(index) > k:
    print(-1)
    quit()
count = 0
while k > len(index):
    if count in index:
        index.remove(count)
    s[count] = 9
    s[(count + 1) * -1] = 9
    count += 1
    k -= 2
for x in index:
    if k == len(index) * 2:
        s[x] = 9
        s[(x + 1) * -1] = 9
        k -= 2
    else:
        if s[x] > s[(x + 1) * -1]:
            s[(x + 1) * -1] = s[x]
        else:
            s[x] = s[(x + 1) * -1]
        k -= 1
count = 0
print(s)
while k > 0:
    if s[count] != 9:
        print("yes")
        s[count] = 9
        s[(count + 1) * -1] = 9
        k -= 2
    count += 1
print(''.join(list(map(str, s))))