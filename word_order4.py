n = int(input())
unique_words = []
word_count = []

for x in range(n):
    current = input()
    if current not in unique_words:
        unique_words.append(current)
        word_count.append(1)
    else:
        word_count[unique_words.index(current)] += 1

print(len(unique_words))
for x in word_count:
    print(x, end = " ")