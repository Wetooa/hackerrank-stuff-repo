n = int(input())
word_count = []
words = []

for x in range(n):
    current = input()
    if current in words:
        word_count[words.index(current)] += 1
    else:
        words.append(current)
        word_count.append(1)
    

print(len(words))
for x in word_count:
    print(x, end = " ")