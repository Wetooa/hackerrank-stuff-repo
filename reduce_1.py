n = 31201
#a = []
#for x in str(n):
#    if x == "0":pass
#    else:print(int(x)-1, end = "")

print(''.join(list(filter(lambda x: int(x) >= 0, [str(int(x)-1) for x in str(n)]))))
# print(int(int((''.join(a))) - (10 ** len(a) - 1) / 9))