def solution(info, n, m):
    num_items = len(info)

    # 초기 상태: A와 B의 흔적이 모두 0인 상태만 True
    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True

    for i in range(num_items):
        a_cost, b_cost = info[i]
        new_dp = [[False] * m for _ in range(n)]

        for a in range(n):
            for b in range(m):
                if not dp[a][b]:
                    continue

                # i번째 물건을 A가 훔치는 경우
                new_a = a + a_cost
                if new_a < n:
                    new_dp[new_a][b] = True

                # i번째 물건을 B가 훔치는 경우
                new_b = b + b_cost
                if new_b < m:
                    new_dp[a][new_b] = True

        dp = new_dp  # 상태 업데이트

    # 가능한 모든 상태 중 A의 흔적이 최소인 값을 찾기
    for a in range(n):
        for b in range(m):
            if dp[a][b]:
                return a

    return -1
