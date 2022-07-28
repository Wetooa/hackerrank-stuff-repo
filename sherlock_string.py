import itertools

def possible(array):    
    # itertools the list and checks if its length results in 1. 1 means that the value was repeated making the list automatically possible
    # if the said function results in a 2, it could mean that removing one character could make it good so it checks for that as well
    # if the said function results in a 3 or more, that automatically means it isn't possible as you would have to remove at least 2 chraracters on the list
    array_iter = []
    for x, y in itertools.groupby(array):
        array_iter.append(len(list(y)))
    if len(array_iter) == 1:
        return "YES"
    if len(array_iter) == 2 and (min(array_iter) == 1 or max(array_iter) == 1):
        if array.count(max(array)) < array.count(min(array)):
            if max(array) - 1 == min(array):
                return "YES"
        elif array.count(max(array)) > array.count(min(array)):
            if min(array) - 1 == 0:
                return "YES"
    return "NO"

# so basically i was wrong, itertools sorts it like this -> [(('a', 2), <itertools bullshit>), (('b', 3), <itertools bullshit>)]

# takes a string and turns it to an dict like array that contains each element along with its occurence
string = itertools.groupby(sorted(input().strip()))
array = []
for x, y in string:
    array.append(len(list(y)))

# sorts said list in descending order
array = sorted(array, reverse=True)
print(possible(array))