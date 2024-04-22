import time
import matplotlib.pyplot as plt

# function 01
def collatz(n):
    clist = [n]
    while True:
        if n == 1:
            return len(clist), clist
        elif n % 2 == 0:
            n = n // 2
            clist.append(n)
        else:
            n = (3 * n) + 1
            clist.append(n)

def longest_collatz_sequence_01(require):
    max_length = 0
    max_collatz = []
    for i in range(2, require + 1):
        tmp_length, collatz_list = collatz(i)

        if max_length < tmp_length:
            max_length = tmp_length
            max_collatz = collatz_list[:]
    
    # print(f"Longest Collatz Sequence : {max_collatz[0]}\nLength : {len(max_collatz)}\nfactors : {max_collatz}")
    return len(max_collatz)


# function 03
def collatz_sequence_length(n, cache):
    if n == 1:
        return 1
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        length = collatz_sequence_length(n // 2, cache) + 1
    else:
        length = collatz_sequence_length(3 * n + 1, cache) + 1
    cache[n] = length
    # print(f"Cache after calculating collatz_sequence_length({n}): {cache}")
    return length

def longest_collatz_sequence_03(require):
    max_length = 0
    max_collatz = 0
    cache = {}  # 다이나믹 프로그래밍을 위한 캐시
    for i in range(2, require + 1):
        length = collatz_sequence_length(i, cache)
        if length > max_length:
            max_length = length
            max_collatz = i
    # print(f"Longest Collatz Sequence starting from {max_collatz} with length {max_length}")
    return max_length


# require = 100

# longest_collatz_sequence_01(require)
# longest_collatz_sequence_03(require)


def measure_time(func, arg):
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    set_time = end_time - start_time
    return set_time

require_list = [100, 10000, 1000000]
time_list_01 = []
time_list_02 = []

for require in require_list:
    time_01 = measure_time(longest_collatz_sequence_01, require)
    time_list_01.append(time_01)
    
    time_02 = measure_time(longest_collatz_sequence_03, require)
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