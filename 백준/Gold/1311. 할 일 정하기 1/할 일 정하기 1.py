import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    dp = [float('inf')] * (1 << N)
    dp[0] = 0

    for mask in range(1 << N):
        x = bin(mask).count('1')  # 현재까지 할당한 사람 수
        for j in range(N):
            if not (mask & (1 << j)):  # j번째 일이 아직 할당되지 않았다면
                dp[mask | (1 << j)] = min(dp[mask | (1 << j)], dp[mask] + cost[x][j])

    print(dp[(1 << N) - 1])

solve()
