import sys
sys.setrecursionlimit(10000)

MAX = 10**9 + 1

# 조합 계산용 메모이제이션
dp = [[-1] * 201 for _ in range(201)]

def comb(n, r):
    if r == 0 or r == n:
        return 1
    if r == 1:
        return n
    if dp[n][r] != -1:
        return dp[n][r]
    val = comb(n - 1, r - 1) + comb(n - 1, r)
    dp[n][r] = min(val, MAX)  # overflow 방지
    return dp[n][r]

def make_word(n, m, k):
    if n == 0:
        return 'z' * m
    if m == 0:
        return 'a' * n

    cnt = comb(n + m - 1, n - 1)
    if k <= cnt:
        return 'a' + make_word(n - 1, m, k)
    else:
        return 'z' + make_word(n, m - 1, k - cnt)

def solve():
    N, M, K = map(int, input().split())
    total = comb(N + M, N)
    if K > total:
        print(-1)
    else:
        print(make_word(N, M, K))

solve()
