n, l = int(input()), []
for x in range(n):
    str = input()
    if "@" in str and "." in str:
        l.append(str)

print(list(filter(lambda x:(x[0:x.index("@")]).isalnum() or ["-", "_"] in x[0:x.index("@")], l)))