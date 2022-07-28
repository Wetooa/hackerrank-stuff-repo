input = input()

#for x in range(200):
 #   if chr(x) == "1":
  #      print("here" + str(x))
   # if chr(x) == "A":
    #    print("here" + str(x))
#    print(chr(x))
 #   if chr(x) == "z":
  #      print("here" + str(x))
   # if chr(x) == "9":
    #    print("here" + str(x))

lowercase = []
uppercase = []
odd_numbers = []
even_numbers = []

for x in input:
    if ord(x) >= 49 and ord(x) <= 58:
        if int(x) % 2 == 0:
            if len(even_numbers) == 0:
                even_numbers.append(x)
            else:
                for y in range(len(even_numbers)):
                    if even_numbers[y] >= x:
                        even_numbers.insert(y, x)
                        break
        else:
            if len(odd_numbers) == 0:
                odd_numbers.append(x)
            else:
                for y in range(len(odd_numbers)):
                    if odd_numbers[y] >= x:
                        odd_numbers.insert(y, x)
                        break
    elif ord(x) >= 65 and ord(x) <= 91:
        if len(uppercase) == 0:
                uppercase.append(x)
        else:
            for y in range(len(uppercase)):
                if ord(uppercase[y]) >= ord(x):
                    uppercase.insert(y, x)
                    break
    elif ord(x) >= 96 and ord(x) <= 122:
        if len(lowercase) == 0:
                lowercase.append(x)
        else:
            for y in range(len(lowercase)):
                if ord(lowercase[y]) >= ord(x):
                    lowercase.insert(y, x)
                    break

print(*(lowercase + uppercase + odd_numbers + even_numbers), sep = "")
print(lowercase)
