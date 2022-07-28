# try to learn lambda, its something similar to calc or math or smth, example -> (lambda x: x + 2)(2) = 4
# sorting values using lambda -> sorted(dic.items(),key= lambda x:x[1]))
# sorting keys using lambda -> sorted(dic.items(),key= lambda x:x[0]))
# add "dict()" ig u want it to be a dictionary type
# btw random shit rani, .title to convert a world to capital, lower or upper for lowercase and uppcase respectively

s = "youtube"
letters = {}

s = ''.join(sorted(s)) # use this shit man iz good, .join to join it, sorts the string alphabetically but turns it into a list so use join lololol

for x in range(len(s)):
    if s[x] not in letters:
        letters[s[x]] = 1
    else:
        letters[s[x]] += 1

letters = dict(sorted(letters.items(), key = lambda x:x[1], reverse = True)) # the 1 inside the bracket shows that im sorting it based on the value
z = list(letters.items())

for x in range(3):
    print(f"{z[x][0]} {z[x][1]}")


# the egotistical version
import itertools


print([[(x + " " + str(y)) for x, y in (sorted([(x, len(list(y))) for (x, y) in (itertools.groupby(sorted([x for x in "pepito"])))], key = lambda x:x[1], reverse = True))][n] for n in range(3)])

