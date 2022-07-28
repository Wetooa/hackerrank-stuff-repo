from typing import Counter


n = int(input().strip())
array = list(map(int, input().strip().split()))
print(len(array) - Counter(array).most_common(1)[0][1])