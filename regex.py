import itertools

n = input()
for q in range(int(n)):
    a = str(input())
    if a[0] not in ["4", "5", "6"]: # starting number checkpoint
        print("Invalid")
        break
    else:
        if "-" in a:
            d = a.replace("-", "")
            try: # all digits checker
                int(d)
            except:
                print("Invalid")
                break

            if len(d) != 16: # less than 16 digits checkpoint
                print("Invalid")
                break
            c = a.split("-")
            for x in c: # more than 4 digits in one hyphen checkpoint
                if len(x) != 4:
                    print("Invalid")
                    break
            b = itertools.groupby(list(''.join(c)))
        else:
            if len(list(a)) != 16: # less than 16 digits checkpoint
                print("Invalid")
                break
            b = itertools.groupby(list(a))
        for x, y in b: # not 4 consecutive digits checkpoint
            if len(list(y)) >= 4:
                print("Invalid")
                break
    print("Valid")
