import sys
input = sys.stdin.read

def count_bits(x):
    return bin(x).count('1')

def solve():
    data = input().split()
    N = int(data[0])
    offset = 1
    cost = []
    for i in range(N):
        row = list(map(int, data[offset + i * N : offset + (i+1) * N]))
        cost.append(row)
    offset += N * N
    status_str = data[offset]
    offset += 1
    P = int(data[offset])

    start_mask = 0
    for i, ch in enumerate(status_str):
        if ch == 'Y':
            start_mask |= (1 << i)

    # 켜진 발전소가 없고 P > 0 이면 불가능
    if count_bits(start_mask) == 0 and P > 0:
        print(-1)
        return

    INF = float('inf')
    dp = [INF] * (1 << N)
    dp[start_mask] = 0

    for mask in range(1 << N):
        if dp[mask] == INF:
            continue
        for i in range(N):
            if not (mask & (1 << i)):
                continue  # i 발전소가 켜져 있는 발전소만 사용 가능
            for j in range(N):
                if mask & (1 << j):
                    continue  # 이미 켜진 발전소는 건너뜀
                next_mask = mask | (1 << j)
                dp[next_mask] = min(dp[next_mask], dp[mask] + cost[i][j])

    result = INF
    for mask in range(1 << N):
        if count_bits(mask) >= P:
            result = min(result, dp[mask])

    print(result if result != INF else -1)

solve()
