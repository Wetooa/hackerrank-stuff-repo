# instead of this, u can use map to make it integers instantly
# n, k = input().split(" ")
# main_array = sorted(input().split(" "), key = lambda x:int(x), reverse=True)

n, k = map(int, input().split(" "))
numbers = map(int, input().split(" "))

# moreover, u can create an array with empty slots with lets say 0 using the * operator

counts = [0] * k
for number in numbers:
    counts[number % k] += 1

count = min(counts[0], 1)
for i in range(1, k//2+1):
    if i != k - i:
        count += max(counts[i], counts[k-i])
if k % 2 == 0: 
    count += 1

print(count)