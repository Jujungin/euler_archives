import time
import matplotlib.pyplot as plt

def largest_palindrome_product_01():
    largest_palindrome = 0
    
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            # 문자열을 뒤집어서 palindrome 인지 확인, 더 큰 palindrome 수가 있으면 저장.
            if str(product) == str(product)[::-1] and product > largest_palindrome:
                largest_palindrome = product
    print(largest_palindrome)
    return largest_palindrome

largest_palindrome_product_01()