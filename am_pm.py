t = input().split(":")
if t[2][2:4] == "PM":
    if t[0] != "12":
        t[0] = str(int(t[0]) + 12)
    if t[0] == "24":
        t[0] = "00"
else:
    if int(t[0]) >= 12:
        t[0] = str(int(t[0]) - 12)
    if len(t[0]) == 1:
        t[0] = "0" + t[0]
t[2] = t[2][0:2]
print(':'.join(t))