q = int(input().strip())
for _ in range(q):
    s = [x for x in input().strip()]
    for x in range(len(s) - 1, 0, -1):
        if s[x] != s[x - 1] and ord(s[x]) > ord(s[x - 1]):
            s[x], s[x - 1] = s[x - 1], s[x]
            print(''.join(s))
            break
        if x == 1:
            print('no answer')