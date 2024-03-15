require = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
require_str = str(require)

require_list = [ 
    [7,  3, 1, 6, 7, 1, 7, 6, 5, 3, 1, 3, 3, 0, 6, 2, 4, 9, 1, 9, 2, 2, 5, 1, 1, 9, 6, 7, 4, 4, 2, 6, 5, 7, 4, 7, 4, 2, 3, 5, 5, 3, 4, 9, 1, 9, 4, 9, 3, 4], 
    [9, 6, 9, 8, 3, 5, 2, 0, 3, 1, 2, 7, 7, 4, 5, 0, 6, 3, 2, 6, 2, 3, 9, 5, 7, 8, 3, 1, 8, 0, 1, 6, 9, 8, 4, 8, 0, 1, 8, 6, 9, 4, 7, 8, 8, 5, 1, 8, 4, 3], 
    [8, 5, 8, 6, 1, 5, 6, 0, 7, 8, 9, 1, 1, 2, 9, 4, 9, 4, 9, 5, 4, 5, 9, 5, 0, 1, 7, 3, 7, 9, 5, 8, 3, 3, 1, 9, 5, 2, 8, 5, 3, 2, 0, 8, 8, 0, 5, 5, 1, 1], 
    [1, 2, 5, 4, 0, 6, 9, 8, 7, 4, 7, 1, 5, 8, 5, 2, 3, 8, 6, 3, 0, 5, 0, 7, 1, 5, 6, 9, 3, 2, 9, 0, 9, 6, 3, 2, 9, 5, 2, 2, 7, 4, 4, 3, 0, 4, 3, 5, 5, 7], 
    [6, 6, 8, 9, 6, 6, 4, 8, 9, 5, 0, 4, 4, 5, 2, 4, 4, 5, 2, 3, 1, 6, 1, 7, 3, 1, 8, 5, 6, 4, 0, 3, 0, 9, 8, 7, 1, 1, 1, 2, 1, 7, 2, 2, 3, 8, 3, 1, 1, 3], 
    [6, 2, 2, 2, 9, 8, 9, 3, 4, 2, 3, 3, 8, 0, 3, 0, 8, 1, 3, 5, 3, 3, 6, 2, 7, 6, 6, 1, 4, 2, 8, 2, 8, 0, 6, 4, 4, 4, 4, 8, 6, 6, 4, 5, 2, 3, 8, 7, 4, 9], 
    [3, 0, 3, 5, 8, 9, 0, 7, 2, 9, 6, 2, 9, 0, 4, 9, 1, 5, 6, 0, 4, 4, 0, 7, 7, 2, 3, 9, 0, 7, 1, 3, 8, 1, 0, 5, 1, 5, 8, 5, 9, 3, 0, 7, 9, 6, 0, 8, 6, 6], 
    [7, 0, 1, 7, 2, 4, 2, 7, 1, 2, 1, 8, 8, 3, 9, 9, 8, 7, 9, 7, 9, 0, 8, 7, 9, 2, 2, 7, 4, 9, 2, 1, 9, 0, 1, 6, 9, 9, 7, 2, 0, 8, 8, 8, 0, 9, 3, 7, 7, 6], 
    [6, 5, 7, 2, 7, 3, 3, 3, 0, 0, 1, 0, 5, 3, 3, 6, 7, 8, 8, 1, 2, 2, 0, 2, 3, 5, 4, 2, 1, 8, 0, 9, 7, 5, 1, 2, 5, 4, 5, 4, 0, 5, 9, 4, 7, 5, 2, 2, 4, 3], 
    [5, 2, 5, 8, 4, 9, 0, 7, 7, 1, 1, 6, 7, 0, 5, 5, 6, 0, 1, 3, 6, 0, 4, 8, 3, 9, 5, 8, 6, 4, 4, 6, 7, 0, 6, 3, 2, 4, 4, 1, 5, 7, 2, 2, 1, 5, 5, 3, 9, 7], 
    [5, 3, 6, 9, 7, 8, 1, 7, 9, 7, 7, 8, 4, 6, 1, 7, 4, 0, 6, 4, 9, 5, 5, 1, 4, 9, 2, 9, 0, 8, 6, 2, 5, 6, 9, 3, 2, 1, 9, 7, 8, 4, 6, 8, 6, 2, 2, 4, 8, 2], 
    [8, 3, 9, 7, 2, 2, 4, 1, 3, 7, 5, 6, 5, 7, 0, 5, 6, 0, 5, 7, 4, 9, 0, 2, 6, 1, 4, 0, 7, 9, 7, 2, 9, 6, 8, 6, 5, 2, 4, 1, 4, 5, 3, 5, 1, 0, 0, 4, 7, 4], 
    [8, 2, 1, 6, 6, 3, 7, 0, 4, 8, 4, 4, 0, 3, 1, 9, 9, 8, 9, 0, 0, 0, 8, 8, 9, 5, 2, 4, 3, 4, 5, 0, 6, 5, 8, 5, 4, 1, 2, 2, 7, 5, 8, 8, 6, 6, 6, 8, 8, 1], 
    [1, 6, 4, 2, 7, 1, 7, 1, 4, 7, 9, 9, 2, 4, 4, 4, 2, 9, 2, 8, 2, 3, 0, 8, 6, 3, 4, 6, 5, 6, 7, 4, 8, 1, 3, 9, 1, 9, 1, 2, 3, 1, 6, 2, 8, 2, 4, 5, 8, 6], 
    [1, 7, 8, 6, 6, 4, 5, 8, 3, 5, 9, 1, 2, 4, 5, 6, 6, 5, 2, 9, 4, 7, 6, 5, 4, 5, 6, 8, 2, 8, 4, 8, 9, 1, 2, 8, 8, 3, 1, 4, 2, 6, 0, 7, 6, 9, 0, 0, 4, 2], 
    [2, 4, 2, 1, 9, 0, 2, 2, 6, 7, 1, 0, 5, 5, 6, 2, 6, 3, 2, 1, 1, 1, 1, 1, 0, 9, 3, 7, 0, 5, 4, 4, 2, 1, 7, 5, 0, 6, 9, 4, 1, 6, 5, 8, 9, 6, 0, 4, 0, 8], 
    [0, 7, 1, 9, 8, 4, 0, 3, 8, 5, 0, 9, 6, 2, 4, 5, 5, 4, 4, 4, 3, 6, 2, 9, 8, 1, 2, 3, 0, 9, 8, 7, 8, 7, 9, 9, 2, 7, 2, 4, 4, 2, 8, 4, 9, 0, 9, 1, 8, 8], 
    [8, 4, 5, 8, 0, 1, 5, 6, 1, 6, 6, 0, 9, 7, 9, 1, 9, 1, 3, 3, 8, 7, 5, 4, 9, 9, 2, 0, 0, 5, 2, 4, 0, 6, 3, 6, 8, 9, 9, 1, 2, 5, 6, 0, 7, 1, 7, 6, 0, 6], 
    [0, 5, 8, 8, 6, 1, 1, 6, 4, 6, 7, 1, 0, 9, 4, 0, 5, 0, 7, 7, 5, 4, 1, 0, 0, 2, 2, 5, 6, 9, 8, 3, 1, 5, 5, 2, 0, 0, 0, 5, 5, 9, 3, 5, 7, 2, 9, 7, 2, 5], 
    [7, 1, 6, 3, 6, 2, 6, 9, 5, 6, 1, 8, 8, 2, 6, 7, 0, 4, 2, 8, 2, 5, 2, 4, 8, 3, 6, 0, 0, 8, 2, 3, 2, 5, 7, 5, 3, 0, 4, 2, 0, 7, 5, 2, 9, 6, 3, 4, 5, 0]
]

def largest_product_01(require,  num):
    greatest_product = 0
    for i in range(len(require) - num - 1):
        product = 1
        if int(require_str[i]) == 0:
            continue
        for j in range(num):
            product *= int(require_str[i+j])
        greatest_product = max(greatest_product,  product)
    return greatest_product


def largest_product_02(require,  num):
    greatest_product = 0
    adjacent_digit = ""
    for i in range(len(require) - (num - 1)):
        product = 1
        temp = require[i:i+num]
        if '0' in temp:
            continue
        for j in temp:
            product *= int(j)
        if greatest_product < product:
            greatest_product = product
            adjacent_digit = temp
            pass
    return greatest_product, adjacent_digit


# 만약 50*20 list이면?
def largest_product_03(require, num):
    greatest_product = 0
    adjacent_digit = ""
    for i in range(len(require)):
        for j in range(len(require[i])):
            # 가로
            if j + (num - 1) < len(require[i]):
                product = 1
                temp = ""
                for k in range(num):
                    if require[i][j+k] == 0:
                        break
                    product *= require[i][j+k]
                    temp += f"{str(require[i][j+k])}"
                greatest_product = max(greatest_product, product)
                adjacent_digit = temp
            
            # 세로
            if i + (num - 1) < len(require):
                product = 1
                temp = ""
                for k in range(num):
                    if require[i+k][j] == 0:
                        break
                    product *= require[i+k][j]
                    temp += f"{str(require[i+k][j])}"
                greatest_product = max(greatest_product, product)
                adjacent_digit = temp

            # 대각(우하)
            if i + (num - 1) < len(require) and j + (num - 1) < len(require[i]):
                product = 1
                temp = ""
                for k in range(num):
                    if require[i+k][j+k] == 0:
                        break
                    product *= require[i+k][j+k]
                    temp += f"{str(require[i+k][j+k])}"
                greatest_product = max(greatest_product, product)
                adjacent_digit = temp
            
            # 대각(우상)
            if i + (num - 1) > 0 and j + (num - 1) < len(require[i]):
                product = 1
                temp = ""
                for k in range(num):
                    if require[i-k][j+k] == 0:
                        break
                    product *= require[i-k][j+k]
                    temp += f"{str(require[i-k][j+k])}"
                greatest_product = max(greatest_product, product)
                adjacent_digit = temp
    return greatest_product, adjacent_digit


# GPT 최대 효율
def find_max_product(matrix, num):
    max_product = 0
    rows = len(matrix)
    cols = len(matrix[0])

    # 가로 방향 최대 곱 계산
    for i in range(rows):
        for j in range(cols - num + 1):
            if 0 in matrix[i][j:j+num]:  # 연속된 숫자에 0이 있는 경우 pass
                continue
            product = 1
            for k in range(num):
                product *= matrix[i][j + k]
            max_product = max(max_product, product)

    # 세로 방향 최대 곱 계산
    for i in range(rows - num + 1):
        for j in range(cols):
            if 0 in [matrix[i+k][j] for k in range(num)]:  # 연속된 숫자에 0이 있는 경우 pass
                continue
            product = 1
            for k in range(num):
                product *= matrix[i + k][j]
            max_product = max(max_product, product)

    # 대각선 (우측 하향) 방향 최대 곱 계산
    for i in range(rows - num + 1):
        for j in range(cols - num + 1):
            if 0 in [matrix[i+k][j+k] for k in range(num)]:  # 연속된 숫자에 0이 있는 경우 pass
                continue
            product = 1
            for k in range(num):
                product *= matrix[i + k][j + k]
            max_product = max(max_product, product)

    # 대각선 (우측 상향) 방향 최대 곱 계산
    for i in range(num - 1, rows):
        for j in range(cols - num + 1):
            if 0 in [matrix[i-k][j+k] for k in range(num)]:  # 연속된 숫자에 0이 있는 경우 pass
                continue
            product = 1
            for k in range(num):
                product *= matrix[i - k][j + k]
            max_product = max(max_product, product)

    return max_product

require_num = 4
print("01: ", largest_product_01(require_str, require_num))
print("02: ", largest_product_02(require_str, require_num))
print("03: ", largest_product_03(require_list, require_num))
