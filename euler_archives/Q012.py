def highly_divisible_triangular_number_01(require):
    natural_num = 1
    sum_of_natural_num = 1
    while True:
        factor = []
        for i in range(1, sum_of_natural_num + 1):
            if int(sum_of_natural_num) % i == 0:
                factor.append(i)
            
        if len(factor) > require:
            print(f"natural number: {natural_num}\nsum of natural: {sum_of_natural_num}\nfactor: {factor}")
            break
        natural_num += 1
        sum_of_natural_num += natural_num

def factor_count(triangular_num):
    count = 0
    for i in range(1, int(triangular_num**0.5) + 1):
        if triangular_num % i == 0:
            count += 2
    return count
    pass

def highly_divisible_triangular_number_02(require):
    natural_num = 1
    while True:
        triangular_num = (natural_num * (natural_num + 1)) // 2
        if factor_count(triangular_num) > require:
            print(triangular_num)
            break
        natural_num += 1
    pass


require = 5
highly_divisible_triangular_number_01(require)
highly_divisible_triangular_number_02(require)


