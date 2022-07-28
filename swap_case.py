def swap_case(s):
    return (''.join([x.lower() if x.isupper() else x.upper() for x in s])) # shit so cool dunno how it fucking works tho

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)