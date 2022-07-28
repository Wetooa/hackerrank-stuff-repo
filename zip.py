# Enter your code here. Read input from STDIN. Print output to STDOUT

a = input().split(" ")[1]
b = []
for _ in range(int(a)):
    b.append([float(x) for x in input().split(" ")])
b = zip(*b)
print('\n'.join([str(sum(x) / int(a)) for x in b]))
