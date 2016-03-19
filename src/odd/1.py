import math

def sumArithmeticSequence(firstTerm, numberOfTerm, difference):
    return (2 * firstTerm + (numberOfTerm - 1) * difference) * numberOfTerm / 2

scope = 1000 - 1

sumOf3Mutiples = sumArithmeticSequence(3, int(scope/3), 3)
sumOf5Mutiples = sumArithmeticSequence(5, int(scope/5), 5)
sumOf15Mutiples = sumArithmeticSequence(15, int(scope/15), 15)

sumOF3Or5Multiples = sumOf3Mutiples + sumOf5Mutiples - sumOf15Mutiples

print(sumOF3Or5Multiples)
