def solution(price, money, count):
    total_cost = price * count * (count + 1) // 2  # 등차수열 합 공식
    return max(0, total_cost - money)
