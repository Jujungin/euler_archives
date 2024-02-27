import time
import matplotlib.pyplot as plt

def largest_prime_factors_01(require):
    # 소수를 저장할 리스트
    prime_factors = []
    # n이 소수가 아닐 때까지 반복
    while require % 2 == 0:
        prime_factors.append(2)
        require //= 2
        # print("01_require(%2): ", require)
    # n은 이제 홀수이므로 3부터 제곱근까지 소인수를 찾음
    # n의 제곱근보다 큰 소인수는 없음
    for i in range(3, int(require**0.5) + 1, 2):
        while require % i == 0:
            prime_factors.append(i)
            require //= i
            # print("01_require(%i): ", require)
    # n이 2보다 큰 경우는 마지막 소수를 추가해줌
    if require > 2:
        prime_factors.append(require)
    # 가장 큰 소인수 반환
    # print(prime_factors)
    # print(max(prime_factors))

def largest_prime_factors_02(require):
    # 2로 나누어 떨어지는만큼 나눈다.
    while require % 2 == 0:
        largest_prime = 2
        require //= 2

    # 제곱근 이하의 홀수로 나누어 떨어지는 소수를 찾는다.
    p = 3
    while p * p <= require:
        while require % p == 0:
            largest_prime = p
            require //= p
        p += 2

    # 남은 수가 1보다 크면 그 수 자체가 소수이다.
    if require > 1:
        largest_prime = require

    # print("02: ",largest_prime)


require = 600851475143
# largest_prime_factors_01(require)
# print("---")
# largest_prime_factors_02(require)

def measure_time(func, arg):
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    set_time = end_time - start_time
    return set_time

require_list = [10, 100, 1000, 10000, 100000, 1000000]
time_list_01 = []
time_list_02 = []

for require in require_list:
    time_01 = measure_time(largest_prime_factors_01, require)
    time_list_01.append(time_01)
    
    time_02 = measure_time(largest_prime_factors_02, require)
    time_list_02.append(time_02)

plt.plot(require_list, time_list_01, color='b', linestyle='-', linewidth=4, label='Function 01')
plt.plot(require_list, time_list_02, color='r', linestyle='-', linewidth=2, label='Function 02')
plt.xlabel('require', fontsize=10)
plt.ylabel('Time (s)', fontsize=10)
plt.title('Time Complexity', fontsize=12)
# plt.xticks(require_list, ['{:,.0f}'.format(num) for num in require_list], fontsize=10)
# plt.xticks(require_list, ['{:,.0e}'.format(num) for num in require_list], fontsize=5)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend(fontsize=10)
plt.show()
