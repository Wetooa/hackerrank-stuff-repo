# eval function is used to evaluate strings and turn them into python expressions
# use (" ", 1) to split a string once, but this time its better to use this, * takes the rest of the splitted string and adds it to list b
# print ''.join([i.lower() if i.isupper() else i.upper() for i in raw_input()]) -----> random shit but learn this one liner man iz cool

n = int(input())

l = []
for _ in range(n):
    a = input().split() 
    cmd = a[0]
    arguments = a[1: ]
    if cmd == "print":
        print(l)
    else:
        eval("l." + cmd + "(" + ', '.join(arguments) + ")")