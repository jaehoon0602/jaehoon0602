import math

def solution(n):
    x = math.isqrt(n)  # 제곱근의 정수값
    if x * x == n:
        return (x + 1) ** 2
    else:
        return -1
