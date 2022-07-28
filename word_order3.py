n = int(input())
words = []
unique_words = []
word_count = []

for x in range(n):
    words.append(input())

while len(words) != 0:
    current = words[0]
    if current not in unique_words:
        unique_words.append(current)
        word_count.append(words.count(current))
    while current in words:
        words.remove(current)

print(len(unique_words))
for x in word_count:
    print(x, end = " ")
        