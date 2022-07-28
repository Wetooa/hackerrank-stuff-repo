n = int(input())
words = []
word_count = []
current = ""

for x in range(n):
    current = input()
    if current not in words:
        words.append(current)
        word_count.append(1)
    else:
        word_count[words.index(current)] += 1

print(len(words))
for x in word_count:
    print(x, end = " ")