import time
import matplotlib.pyplot as plt
import random

require_adjacent = 4
require = [
    ["08", "02", "22", "97", "38", "15", "00", "40", "00", "75", "04", "05", "07", "78", "52", "12", "50", "77", "91", "08"],
    ["49", "49", "99", "40", "17", "81", "18", "57", "60", "87", "17", "40", "98", "43", "69", "48", "04", "56", "62", "00"],
    ["81", "49", "31", "73", "55", "79", "14", "29", "93", "71", "40", "67", "53", "88", "30", "03", "49", "13", "36", "65"],
    ["52", "70", "95", "23", "04", "60", "11", "42", "69", "24", "68", "56", "01", "32", "56", "71", "37", "02", "36", "91"],
    ["22", "31", "16", "71", "51", "67", "63", "89", "41", "92", "36", "54", "22", "40", "40", "28", "66", "33", "13", "80"],
    ["24", "47", "32", "60", "99", "03", "45", "02", "44", "75", "33", "53", "78", "36", "84", "20", "35", "17", "12", "50"],
    ["32", "98", "81", "28", "64", "23", "67", "10", "26", "38", "40", "67", "59", "54", "70", "66", "18", "38", "64", "70"],
    ["67", "26", "20", "68", "02", "62", "12", "20", "95", "63", "94", "39", "63", "08", "40", "91", "66", "49", "94", "21"],
    ["24", "55", "58", "05", "66", "73", "99", "26", "97", "17", "78", "78", "96", "83", "14", "88", "34", "89", "63", "72"],
    ["21", "36", "23", "09", "75", "00", "76", "44", "20", "45", "35", "14", "00", "61", "33", "97", "34", "31", "33", "95"],
    ["78", "17", "53", "28", "22", "75", "31", "67", "15", "94", "03", "80", "04", "62", "16", "14", "09", "53", "56", "92"],
    ["16", "39", "05", "42", "96", "35", "31", "47", "55", "58", "88", "24", "00", "17", "54", "24", "36", "29", "85", "57"],
    ["86", "56", "00", "48", "35", "71", "89", "07", "05", "44", "44", "37", "44", "60", "21", "58", "51", "54", "17", "58"],
    ["19", "80", "81", "68", "05", "94", "47", "69", "28", "73", "92", "13", "86", "52", "17", "77", "04", "89", "55", "40"],
    ["04", "52", "08", "83", "97", "35", "99", "16", "07", "97", "57", "32", "16", "26", "26", "79", "33", "27", "98", "66"],
    ["88", "36", "68", "87", "57", "62", "20", "72", "03", "46", "33", "67", "46", "55", "12", "32", "63", "93", "53", "69"],
    ["04", "42", "16", "73", "38", "25", "39", "11", "24", "94", "72", "18", "08", "46", "29", "32", "40", "62", "76", "36"],
    ["20", "69", "36", "41", "72", "30", "23", "88", "34", "62", "99", "69", "82", "67", "59", "85", "74", "04", "36", "16"],
    ["20", "73", "35", "29", "78", "31", "90", "01", "74", "31", "49", "71", "48", "86", "81", "16", "23", "57", "05", "54"],
    ["01", "70", "54", "71", "83", "51", "54", "69", "16", "92", "33", "48", "61", "43", "52", "01", "89", "19", "67", "48"]
]

def random_require_list(size):
    return [[str(random.randint(0, 99)).zfill(2) for _ in range(size)] for _ in range(size)]

def largest_product_in_a_grid(require, require_adjacent):
    # int 변환 (list comprehension)
    require = [[int(x) for x in row] for row in require]
    largest_product = []
    largest = 0
    
    for i in range(len(require)):
        for j in range(len(require[0])):
            #가로
            if j + require_adjacent <= len(require[0]):
                tmp = 1
                largest_product_tmp = []
                for k in range(require_adjacent):
                    if require[i][j + k] == 0:
                        break
                    tmp *= require[i][j + k]
                    largest_product_tmp.append(require[i][j+k])
                # largest = max(largest, tmp)
                if largest < tmp:
                    largest = tmp
                    largest_product = largest_product_tmp

            # 세로
            if i + require_adjacent <= len(require):
                tmp = 1
                largest_product_tmp = []
                for k in range(require_adjacent):
                    if require[i + k][j] == 0:
                        break
                    tmp *= require[i + k][j]
                    largest_product_tmp.append(require[i + k][j])
                # largest = max(largest, tmp)
                if largest < tmp:
                    largest = tmp
                    largest_product = largest_product_tmp 

            # 대각 우상
            if i - require_adjacent >= 0 and j + require_adjacent <= len(require[0]):
                tmp = 1
                largest_product_tmp = []
                for k in range(require_adjacent):
                    if require[i - k][j + k] == 0:
                        break
                    tmp *= require[i - k][j + k]
                    largest_product_tmp.append(require[i - k][j + k])
                # largest = max(largest, tmp)
                if largest < tmp:
                    largest = tmp
                    largest_product = largest_product_tmp

            # 대각 우하
            if i + require_adjacent <= len(require) and j + require_adjacent <= len(require[0]):
                tmp = 1
                largest_product_tmp = []
                for k in range(require_adjacent):
                    if require[i + k][j + k] == 0:
                        break
                    tmp *= require[i + k][j + k]
                    largest_product_tmp.append(require[i + k][j + k])
                # largest = max(largest, tmp)
                if largest < tmp:
                    largest = tmp
                    largest_product = largest_product_tmp
    
    return largest, largest_product


def largest_product_in_a_grid_enhanced(require, require_adjacent):
    require = [[int(x) for x in row] for row in require]
    largest = 0
    largest_product = []

    def calculate_product(nums):
        product = 1
        for num in nums:
            if num == 0:
                return 0, []
            product *= num
        return product, nums

    # 가로 방향 계산
    for i in range(len(require)):
        for j in range(len(require[0]) - require_adjacent + 1):
            product, product_nums = calculate_product(require[i][j:j + require_adjacent])
            if product > largest:
                largest = product
                largest_product = product_nums

    # 세로 방향 계산
    for j in range(len(require[0])):
        for i in range(len(require) - require_adjacent + 1):
            product, product_nums = calculate_product([require[i + k][j] for k in range(require_adjacent)])
            if product > largest:
                largest = product
                largest_product = product_nums

    # 대각선 방향 계산 (우상향)
    for i in range(len(require) - require_adjacent + 1):
        for j in range(len(require[0]) - require_adjacent + 1):
            product, product_nums = calculate_product([require[i + k][j + k] for k in range(require_adjacent)])
            if product > largest:
                largest = product
                largest_product = product_nums

    # 대각선 방향 계산 (우하향)
    for i in range(len(require) - 1, require_adjacent - 2, -1):
        for j in range(len(require[0]) - require_adjacent + 1):
            product, product_nums = calculate_product([require[i - k][j + k] for k in range(require_adjacent)])
            if product > largest:
                largest = product
                largest_product = product_nums

    return largest, largest_product

# largest, largest_product = largest_product_in_a_grid(require, require_adjacent)
# print(f"largest: {largest}, product: {largest_product}")


# largest, largest_product = largest_product_in_a_grid_enhanced(require, require_adjacent)
# print(f"largest: {largest}, product: {largest_product}")


def measure_time(func, arg, arg1):
    start_time = time.time()
    result, result_product = func(arg, arg1)
    end_time = time.time()
    set_time = end_time - start_time
    return set_time

require_sizes = [50, 150, 250, 350]
time_list_01 = []
time_list_02 = []

for size in require_sizes:
    require = random_require_list(size)
    
    time_01 = measure_time(largest_product_in_a_grid, require, require_adjacent)
    time_list_01.append(time_01)

    time_02 = measure_time(largest_product_in_a_grid_enhanced, require, require_adjacent)
    time_list_02.append(time_02)

    

plt.plot(require_sizes, time_list_01, color='b', linestyle='-', linewidth=1, label='Function 01')
plt.plot(require_sizes, time_list_02, color='r', linestyle='-', linewidth=2, label='Function 02')
plt.xlabel('require', fontsize=10)
plt.ylabel('Time (s)', fontsize=10)
plt.title('Time Complexity', fontsize=12)
# plt.xticks(require_list, ['{:,.0f}'.format(num) for num in require_list], fontsize=10)
# plt.xticks(require_list, ['{:,.0e}'.format(num) for num in require_list], fontsize=5)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend(fontsize=10)
plt.show()