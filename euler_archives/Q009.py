import time
import matplotlib.pyplot as plt

def special_pythagorean_triplet_01(require):
    for a in range(1, require):
        for b in range(a + 1, require):
            c = (a**2 + b**2)**0.5
            if c.is_integer() == True and a + b + c == 1000:
                # print(f"{a} + {b} + {c} = {a+b+c}")
                return a * b * c

def special_pythagorean_triplet_02(require):
    for n in range(1, int(require//2)):
        for m in range(n + 1, int(require//2)):
            if m * (m + n) == int(require//2):
                # print(f"m: {m}, n: {n}, a: {m**2 - n**2}, b: {2 * m * n}, c: {m**2 + n**2}, abc: {(m**2 - n**2)*(2 * m * n)*(m**2 + n**2)}")
                return (m**2 - n**2)*(2 * m * n)*(m**2 + n**2)

def special_pythagorean_triplet_03(require):
    for a in range(1, require//3):
        b = (require * (require - (2 * a))) / (2 * (require - a))
        c = require - a - b
        if b == int(b) and c == int(c):
            # print(f"a: {a}, b: {int(b)}, c: {int(c)}, abc: {int(a * b * c)}")
            return a * b * c
            

def measure_time(func, arg):
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    set_time = end_time - start_time
    return set_time

require_list = [10, 100, 1000]
time_list_01 = []
time_list_02 = []
time_list_03 = []

for require in require_list:
    time_01 = measure_time(special_pythagorean_triplet_01, require)
    time_list_01.append(time_01)
    
    time_02 = measure_time(special_pythagorean_triplet_02, require)
    time_list_02.append(time_02)
    
    time_03 = measure_time(special_pythagorean_triplet_03, require)
    time_list_03.append(time_03)

plt.plot(require_list, time_list_01, color='b', linestyle='-', linewidth=1, label='Function 01')
plt.plot(require_list, time_list_02, color='r', linestyle='-', linewidth=2, label='Function 02')
plt.plot(require_list, time_list_03, color='g', linestyle='-.', linewidth=4, label='Function 03')
plt.xlabel('require', fontsize=10)
plt.ylabel('Time (s)', fontsize=10)
plt.title('Time Complexity', fontsize=12)
# plt.xticks(require_list, ['{:,.0f}'.format(num) for num in require_list], fontsize=10)
# plt.xticks(require_list, ['{:,.0e}'.format(num) for num in require_list], fontsize=5)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend(fontsize=10)
plt.show()