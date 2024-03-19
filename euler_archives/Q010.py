def summation_of_prime(require):
    summation = 2
    number = 3
    primes = [2]
    while True:
        is_prime = True 
        for prime in primes:
            if number % prime == 0:
                is_prime = False
                break
            if prime**2 > number:
                break
        
        if is_prime:
            summation += number
            primes.append(number)
            if summation >= require:
                print(f"summation: {summation}")
                print(f"primes: {primes}")
                return summation
                
        number += 2                     

require = 1000000
# require = 20
result = summation_of_prime(require)
print(f"result: {result}")