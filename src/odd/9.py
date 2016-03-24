import math
import datetime

sum = 1000

# a + b + c = sum
# a + b > c
# a + b > sum - a - b
# b > (sum - 2a)/2
# b > a
def getBLowerBound(a):
    return max(math.floor((sum - 2 * a) / 2), a) + 1

# a + b + c = sum
# b < c
# b < sum - b - a
# b < (sum - a)/2
def getBUpperBound(a):
    return math.ceil((sum - a) / 2) - 1

for a in range(1, math.floor((sum - 3) / 3)):
    lowerB = getBLowerBound(a)
    upperB = getBUpperBound(a)

    if lowerB > upperB:
        continue

    for b in range(lowerB, upperB + 1):
        c = sum - a - b

        if a ** 2 + b ** 2 == c ** 2:
            print("a: ", a)
            print("b: ", b)
            print("c: ", c)
            print(a * b *c)
