import time
import matplotlib.pyplot as plt

def sum_of_multiples_01(require):
    result = 0
    for i in range(require):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

def sum_of_multiples_02(require):
    require -= 1
    
    sum_of_3 = 3 * (require // 3) * ((require // 3) + 1) // 2
    sum_of_5 = 5 * (require // 5) * ((require // 5) + 1) // 2
    sum_of_15 = 15 * (require // 15) * ((require // 15) + 1) // 2

    result = sum_of_3 + sum_of_5 - sum_of_15
    return result

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
    time_01 = measure_time(sum_of_multiples_01, require)
    time_list_01.append(time_01)
    
    time_02 = measure_time(sum_of_multiples_02, require)
    time_list_02.append(time_02)

plt.plot(require_list, time_list_01, color='b', linestyle='-', linewidth=2, label='Function 01')
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
