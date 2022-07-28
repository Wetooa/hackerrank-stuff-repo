n = int(input().strip())
string = input().strip()
k = int(input().strip())
new_string = ""
for x in range(n):
    if string[x].isalpha():
        letter = string[x]
        upper = False
        if ord(string[x]) >= 97:
            letter = string[x].upper()
            upper = True
        index = ord(letter) + k
        while index > 90: index -= 26
        if upper == True: new_string += chr(index).lower()
        else: new_string += chr(index)
    else: new_string += string[x]
print(new_string)