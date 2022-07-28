# so I basically, there's this problem in comsci where you check for the possible combiantions in a list
# now making that is easy if the combinations length is fixed ie.

l = [1, 5, 2, 6, 3]

for x in range(len(l)-2):
    for y in range(x+1, len(l)-1):
        for z in range(y+1, len(l)):
            print(l[x], l[y], l[z])

print("")
for x in range(len(l)-1):
    for y in range(x+1, len(l)):
        print(l[x], l[y])

# this checks for the possible combinations made by l using three for loops
# very cool if you ask me
# but if you lets say ask for all the possible combinations in the list
# then that would obviously include pairs or length of 5 combinations
# that one is hard, and there is a problem for that
