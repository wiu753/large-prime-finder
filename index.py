import random

def generate_odd_number(bit_size):
    odd_number = random.randrange(1, 2**bit_size, 2)
    
    while (odd_number.bit_length() != bit_size):
        odd_number = random.randrange(1, 2**bit_size, 2)
    
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


prime_numbers = []
miller_rabin_iterations = 100
solovoy_strassen_iterations = 100
numbers_tested = 0

while (len(prime_numbers) < 2):
    number_to_test = generate_odd_number()
    numbers_tested += 1
    if (solovoy_strassen(number_to_test, solovoy_strassen_iterations) and miller_rabin(number_to_test, miller_rabin_iterations)):
        prime_numbers.append(number_to_test)

print("Prime number one: {} \nPrime number two: {}".format(prime_numbers[0], prime_numbers[1]))
print("Numbers tested: ", numbers_tested)
