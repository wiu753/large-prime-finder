import random

def generateOddNumber():
    odd_number = random.randrange(1, 2**1024, 2)
    
    while (odd_number.bit_length() != 1024):
        odd_number = random.randrange(1, 2**1024, 2)
    
    return odd_number

def isNumberOdd(number):
    if (number % 2 == 0):
        return False
    else:
        return True

x = generateOddNumber()
print(x)
print(x.bit_length())
print(isNumberOdd(x))