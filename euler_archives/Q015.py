# 0, 0 -> 3, 5
require_rows = 3
require_cols = 5

def lattice_paths_01(require_rows, require_cols):
    path = [ [0] * (require_cols + 1) for _ in range(require_rows + 1) ]
    
    for r in range(require_rows + 1):
        path[r][0] = 1
    for c in range(require_cols + 1):
        path[0][c] = 1
    
    for i in range(1, require_rows + 1):
        for j in range(1, require_cols + 1):
            path[i][j] = path[i-1][j] + path[i][j-1]
            
    return path[i][j]

def lattice_paths_02(sum, r):
    prev = [0] * (r + 1)
    prev[0] = 1
    for i in range(1, sum + 1):
        curr = [0] * (r + 1)
        curr[0] = 1
        for j in range(1, min(i, r) + 1):
            curr[j] = prev[j] + prev[j - 1]
        prev = curr
    return prev[r]
    
print(f"result: {lattice_paths_01(require_rows, require_cols)}")
print(f"result: {lattice_paths_02(require_rows + require_cols, require_cols)}")



# def binomial_coefficient(n, k):
#     """
#     이항 계수를 구하는 함수
#     """
#     # k가 0이거나 n과 같으면 항상 1을 반환
#     if k == 0 or k == n:
#         return 1

#     # 파스칼의 삼각형을 이용하여 이항 계수를 구함
#     prev_row = [0] * (k + 1)
#     print(prev_row)
#     prev_row[0] = 1
#     for i in range(1, n + 1):
#         curr_row = [0] * (k + 1)
#         curr_row[0] = 1
#         for j in range(1, min(i, k) + 1):
#             curr_row[j] = prev_row[j] + prev_row[j - 1]
#         prev_row = curr_row

#     return prev_row[k]

# def lattice_paths(n):
#     # 격자의 가로와 세로 길이의 합이 n일 때의 이항 계수를 반환
#     return binomial_coefficient(7, 4)

# # 0,0에서 2,2로 가는 방법의 가짓수를 계산합니다.
# result = lattice_paths(2)
# print("0,0에서 2,2로 가는 방법의 가짓수:", result)
