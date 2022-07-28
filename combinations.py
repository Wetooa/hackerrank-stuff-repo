def combi(a = [], index = 0):
    global answer
    for x in range(index, len(l)):
        a.append(l[x])
        if sum(a) == 6 and len(a) > answer:
            answer = len(a)
        print(a)
        combi(a, x + 1)
        a.pop()

l = [x for x in range(10)]
answer = 0
combi()
print(answer)