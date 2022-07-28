array = list(map(int, input().strip().split()))
word = input().strip()
letters = set()
for x in range(len(word)):
    letters.add(array[ord(word[x]) - 97])
print(max(letters) * len(word))