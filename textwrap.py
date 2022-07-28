import textwrap # to output texts with a max length example input "ABDEDSDSNJFJSKE 4" will result in kinda like a split with only 4 max string in every element yea cool

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)