# any function to check if at least 1 element in a list is true , all() if you want all characters is true

s = input()
print (any(c.isalnum() for c in s))
print (any(c.isalpha() for c in s))
print (any(c.isdigit() for c in s))
print (any(c.islower() for c in s))
print (any(c.isupper() for c in s))