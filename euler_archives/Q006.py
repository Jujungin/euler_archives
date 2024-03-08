import time
import matplotlib.pyplot as plt

def sum_square_difference_01(require):
    sum_of_square = 0
    square_of_sum = 0
    result = 0
    for i in range(1, require+1):
        sum_of_square += i**2
        square_of_sum += i
    result = square_of_sum**2 - sum_of_square
    return result
    pass

def sum_square_difference_02(require):
    sum_of_square = (require * (require + 1) * (2 * require + 1)) // 6
    square_of_sum = ((require * (require + 1)) // 2) ** 2
    result = square_of_sum - sum_of_square
    return result

def measure_time(func, arg):
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    set_time = end_time - start_time
    return set_time

require_list = [10, 100, 1000, 10000]
time_list_01 = []
time_list_02 = []

for require in require_list:
    time_01 = measure_time(sum_square_difference_01, require)
    time_list_01.append(time_01)
    
    time_02 = measure_time(sum_square_difference_02, require)
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