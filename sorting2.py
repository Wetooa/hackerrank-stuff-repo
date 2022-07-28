# sorted() if primarily numbers, a.sort() if u need parameters such as a key (sometimes needs a func) or reverse to reverse the list
# using * will automatically turn a list into a string

input = input()
ord_list = []
even_numbers = []
odd_numbers = []
lowercase = []
uppercase = []

for x in input:
    if x == "0":
        even_numbers.append(x)
    else:
        ord_list.append(ord(x))

ord_list = sorted(ord_list)

for x in ord_list:
    if x >= 49 and x <= 58:
        if x % 2 == 0:
            even_numbers.append(chr(x))
        else:
            odd_numbers.append(chr(x))
    elif x >= 65 and x <= 91:
        uppercase.append(chr(x))
    elif x >= 96 and x <= 122:
        lowercase.append(chr(x))

print(*(lowercase + uppercase + odd_numbers + even_numbers), sep = "")