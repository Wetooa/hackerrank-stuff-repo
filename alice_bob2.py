

def isPrime(i):
    for x in range(2, int(i ** 0.5 + 1)):
        if i % x == 0:
            return False
    return True

def sillyGame(n):
    biggestPrime = prime[-1]
    if n > biggestPrime:
        for i in range(biggestPrime + 1, n + 1):
            if isPrime(i): 
                prime.append(i)
    return 'Alice' if sum(i <= n for i in prime) % 2 else 'Bob'

prime = [2]
for _ in range(int(input().strip())):
    print(sillyGame(int(input().strip())))