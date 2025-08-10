import math

def solution(n, m):
    gcd_value = math.gcd(n, m)              # 최대공약수
    lcm_value = (n * m) // gcd_value        # 최소공배수
    return [gcd_value, lcm_value]

# 테스트
print(solution(3, 12))  # [3, 12]
print(solution(2, 5))   # [1, 10]
