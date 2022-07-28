q = int(input().strip())
for _ in range(q):
    array = list(map(int, input().strip().split()))

    # array[0] = prisoners
    # array[1] = sweets
    # array[2] = starting point

    formula = array[1] % array[0] + (array[2] - 1)
    if formula == 0:
        formula += array[0]
    if formula > array[0]:
        formula %= array[0]
    print(formula)