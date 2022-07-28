# to check for prime numbers, u can use the following code, or u can use import sympy's sympy.isprime() function
# holy crap u can do this with a for loop function?????? u can add an else statement after a for loop function
# if the for loop function breaks, it moves to else statement MIND BLOWNNNNN

q = int(input().strip())
prime = [2]
counter = 3
for _ in range(q):
    n = int(input().strip())
    while n >= counter:
        for x in range(2, int(counter ** 0.5 + 1)):
            if counter % x == 0:
                break
        else:
            prime.append(counter)
        counter += 1

    if sum(i <= n for i in prime) % 2:
        print("Alice")
    else:
        print("Bob")
print(prime)
print(len(prime))