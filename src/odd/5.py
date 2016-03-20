fromNum = 1
toNum = 20

def smallestMultiples(a, b):
    result = 1
    i = 2
    while i <= min(a, b):
        if a % i == 0 and b % i == 0:
            result = i * result
            a = a / i
            b = b / i
        else:
            i = i + 1
    return result * a * b

result = fromNum
for i in range(fromNum + 1, toNum):
    result = smallestMultiples(result, i)

print(result)
