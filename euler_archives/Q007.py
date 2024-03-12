def generate_primes(require):
    primes = [2]
    num = 3
    while True:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
            
            # 에라토스테네스의 체
            if prime**2 > num:
                break
        if is_prime:
            primes.append(num)
            if len(primes) == require:
                return primes[-1]
        num += 2

result = generate_primes(10001)
print(result)
