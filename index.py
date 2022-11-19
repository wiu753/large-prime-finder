import random

def generate_odd_number():
    odd_number = random.randrange(1, 2**1024, 2)
    
    while (odd_number.bit_length() != 1024):
        odd_number = random.randrange(1, 2**1024, 2)
    
    return odd_number

def isNumberOdd(number):
    if (number % 2 == 0):
        return False
    else:
        return True

def miller_rabin(number, iterations):
    if (number == 2):
        return True
    if (number == 1 or number % 2 == 0):
        return False
    
    # Find r and s
    r = 0
    s = number - 1
    while (s % 2 == 0):
        r += 1
        s //= 2
    
    for i in range(iterations):
        a = random.randrange(2, number - 1)
        x = pow(a, s, number)
        if (x == 1 or x == number - 1):
            continue
        
        for j in range(r - 1):
            x = pow(x, 2, number)
            if (x == number - 1):
                break
        else:
            return False
    
    return True

def solovoy_strassen(number, iterations):
    if (number == 2):
        return True
    if (number == 1 or number % 2 == 0):
        return False
    
    for i in range(iterations):
        a = random.randrange(2, number - 1)
        if (pow(a, (number - 1) // 2, number) == number - 1):
            continue
        
        if (pow(a, (number - 1) // 2, number) != 1):
            return False
    
    return True

test = generate_odd_number()
print(test)
print(isNumberOdd(test))
print(test.bit_length())

for i in range(1000):
    number = generate_odd_number()
    if (miller_rabin(number, 100)):
        print("Miller Rabin: Prime number is {}".format(number))
        break

for i in range(1000):
    number = generate_odd_number()
    if (solovoy_strassen(number, 100)):
        print("Solowoy Strassen: Prime number is {}".format(number))
        break