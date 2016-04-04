def getNumberWord(n):
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    decimals = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    word = ''
    if n < 10:
        word = units[n]
    elif n >= 10 and n < 20:
        word = teens[n % 10]
    elif n >= 20 and n < 100:
        word = decimals[n // 10] + units[n % 10]
    elif n >= 100 and n < 1000:
        word = units[n // 100] + 'hundred'
        divident = n % 100
        if divident != 0:
            word += 'and' + getNumberWord(divident)
    elif n == 1000:
        word = 'onethousand'

    return word

length = 0
for i in range(1, 1001):
    length += len(getNumberWord(i))

print(length)
