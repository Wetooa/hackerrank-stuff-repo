# n = int(input())
# array = sorted(input().split())

n = int(input())
array = [1 if int(x) > 0 else 0 if int(x) == 0 else -1 for x in input().split(" ")]
print("{0:.6f}".format(array.count(1)/n))
print("{0:.6f}".format(array.count(-1)/n))
print("{0:.6f}".format(array.count(0)/n))