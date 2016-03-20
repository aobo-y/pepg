import math

order = 10001

def ifPrimeNumber(n):
    limit = math.floor(math.sqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True

n = 2
i = 0
while i < order:
    if ifPrimeNumber(n):
        i = i + 1
        lastPrimeNumber = n
    n = n + 1

print(lastPrimeNumber)
