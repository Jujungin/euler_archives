# euler_archives
---
## 001. Multiples of 3 or 5
> Q. If we list all the natural numbers below  10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.
1. 간단하게 조건문으로 해결
```python
for 범위
    if 3, 5의 배수
```
3. 수학적 계산
등차수열의 합을 구하는 문제로 3의 배수와 5의 배수를 각각 따로 계산한 뒤, 중복되는 부분을 제거
```python
sum_3의 배수
+ sum_5의 배수
- sum_3*5의 배수
```
