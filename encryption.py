import math
from re import L

s = "if man was meant to stay on the ground god would have given us roots"

s = s.replace(" ", "")
f = math.floor(math.sqrt(len(s)))
c = math.ceil(math.sqrt(len(s)))

for x in range(c):
    print(s[x::c], end = " ")