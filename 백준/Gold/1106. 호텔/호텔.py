import sys

def min_cost_to_get_customers(C, cities):
    MAX_CUSTOMERS = C + 100  # 여유 있게 설정
    INF = float('inf')
    dp = [INF] * (MAX_CUSTOMERS + 1)
    dp[0] = 0

    for cost, customer in cities:
        for i in range(customer, MAX_CUSTOMERS + 1):
            dp[i] = min(dp[i], dp[i - customer] + cost)

    return min(dp[C:])

# 입력 처리
C, N = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(min_cost_to_get_customers(C, cities))
