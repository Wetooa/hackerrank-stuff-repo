n = input()
words = {} # dictionary very useful, learn how to use properly, set() could also be used

for x in range(int(n)):
    current = input()
    if current in words:
        words[current] += 1
    else:
        words[current] = 1
    
print(len(words))
for x in words:
    print(words[x], end = " ")
