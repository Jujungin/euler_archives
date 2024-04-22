from decimal import Decimal
import time

require = 15

def power_digit_sum_01(require):
    require_str = str(Decimal(2**require))
    result = sum(int(digit) for digit in require_str if digit.isdigit())
    return result

start = time.time()
print(f"power digit sum : {power_digit_sum_01(require)}")
end = time.time()
print(end - start)

def power_digit_sum_02(exponent):
    # 2의 거듭제곱을 문자열로 변환합니다.
    power_str = str(Decimal(2 ** exponent))
    
    # 각 자릿수의 합을 구합니다.
    digit_sum = sum(map(int, power_str))
    
    return digit_sum

require = 15
start = time.time()
print(f"The sum of the digits of 2^{require} is: {power_digit_sum_02(require)}")
end = time.time()
print(end - start)


