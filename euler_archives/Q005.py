import time
import matplotlib.pyplot as plt
import random

def prime_factors(n):
    factors = {}
    divisor = 2
    while n > 1:
        count = 0
        while n % divisor == 0:
            count += 1
            n //= divisor
        if count > 0:
            factors[divisor] = count
        divisor += 1
    return factors

def smallest_multiple_01(n):
    prime_factors_count = {}
    for i in range(2, n+1):
        factors = prime_factors(i)
        for factor, count in factors.items():
            if factor not in prime_factors_count or count > prime_factors_count[factor]:
                prime_factors_count[factor] = count
    result = 1
    for factor, count in prime_factors_count.items():
        result *= factor ** count
    return result

result = smallest_multiple_01(20)
print("result: ", result)
