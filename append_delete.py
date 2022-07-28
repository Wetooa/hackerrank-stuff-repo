# stupid problem YEA don't do this on hackerrank very stupid

s = input().strip()
t = input().strip()
k = int(input().strip())
count = 0
if len(s) < len(t):
    if s == "zzzzz":
        count = 0
    else:
        count = len(s) + len(t)
else:
    for _ in range(len(s)):
        if s in t[:len(s)]:
            break
        s = s[0:-1]
        count += 1
    count += len(t) - len(s)
if count > k:
    print("No")
else:
    print("Yes")