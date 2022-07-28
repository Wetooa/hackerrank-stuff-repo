# if you want to print a list differently, use the * operator and the sep function ie, print(*[1, 2, 3], sep = " ")

def merge_the_tools(string, k):
    for x in range(0, -1*(-(len(string))//k)):
        l = list(string[x*k:x*k+k])
        s = []
        for y in l:
            if y not in s:
                s.append(y)
        print(*(s), sep = "")


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)