import time
import matplotlib.pyplot as plt

def fibonacci_01(require):
    fibonacci_list = [1, 2]
    sum_of_evenNumber = 0
    
    i = 1
    while True:
        if fibonacci_list[i] < require and fibonacci_list[i] % 2 == 0:
            sum_of_evenNumber += fibonacci_list[i]
            pass
        elif fibonacci_list[i] > require:
            # print("sum_of_evenNumber 01: ",sum_of_evenNumber)
            break
        
        fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i-1])
        i += 1
    pass


def fibonacci_02(require):
    a, b = 1, 2
    sum_of_even_number = 0
    
    while b < require:
        if b % 2 == 0:
            sum_of_even_number += b
        a, b = b, a + b
    
    # print("sum of evenNumber 02: ", sum_of_even_number)
    return sum_of_even_number
    pass

# def fibonacci_03(require):
#     def fibonacci_recursive(n):
#         if n <= 1:
#             return n
#         else:
#             return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
#     sum_of_even_number = 0
#     n = 0
#     fib = 0
#     while fib <= require:
#         fib = fibonacci_recursive(n)
#         if fib % 2 == 0:
#             sum_of_even_number += fib
#         n += 1
    
#     return sum_of_even_number
        

def measure_average_time(func, arg, num_trials=1000):
    total_time = 0
    for _ in range(num_trials):
        start_time = time.time()
        func(arg)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / num_trials

require_list = [10, 100, 1000, 10000, 100000, 1000000, 4000000]
# require_list = [10, 100, 1000]
time_list_01 = []
time_list_02 = []
# time_list_03 = []

for require in require_list:
    time_01 = measure_average_time(fibonacci_01, require)
    time_list_01.append(time_01)
    
    time_02 = measure_average_time(fibonacci_02, require)
    time_list_02.append(time_02)
    
    # time_03 = measure_average_time(fibonacci_03, require)
    # time_list_03.append(time_03)



plt.plot(require_list, time_list_01, color='b', linestyle='-', linewidth=5, label='Function 01')
plt.plot(require_list, time_list_02, color='r', linestyle='--', linewidth=2, label='Function 02')
# plt.plot(require_list, time_list_03, color='y', linestyle='-.', linewidth=3, label='Function 03')
plt.xlabel('require', fontsize=10)
plt.ylabel('Time (s)', fontsize=10)
plt.title('Time Complexity', fontsize=12)
# plt.xticks(require_list, ['{:,.0f}'.format(num) for num in require_list], fontsize=10)
# plt.xticks(require_list, ['{:,.0e}'.format(num) for num in require_list], fontsize=5)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend(fontsize=10)
plt.show()