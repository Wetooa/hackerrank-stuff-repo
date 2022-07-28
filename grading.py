import math

def checker(num):
    if num < 38 or math.ceil(num/5)*5 - num > 2:
        return num
    return math.ceil(num/5)*5
         
for x in range(int(input())):
    num = int(input())
    print(checker(num))