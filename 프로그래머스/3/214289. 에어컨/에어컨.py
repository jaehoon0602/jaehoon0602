def solution(temperature, t1, t2, a, b, onboard):
    """
    temperature: int (outdoor)
    t1, t2: int (comfortable inclusive range)
    a, b: int (power costs)
    onboard: list of 0/1, length n (onboard[i]==1 -> passenger at minute i)
    """
    n = len(onboard)
    # dp: dict mapping current indoor temp at minute i -> minimal cost up to minute i
    dp = {temperature: 0}  # minute 0 indoor temp == outdoor temp, cost 0

    def move_towards(x, target):
        if x < target:
            return x + 1
        elif x > target:
            return x - 1
        else:
            return x

    for i in range(n):
        # At minute i, temp must be within [t1, t2] if passenger onboard
        if onboard[i] == 1:
            dp = {temp: cost for temp, cost in dp.items() if t1 <= temp <= t2}
        # Problem guarantees feasibility, but guard anyway
        if not dp:
            # unreachable (shouldn't happen per problem statement)
            return float('inf')

        # Generate next minute (i -> i+1) states
        next_dp = {}
        for temp, cost in dp.items():
            # 1) AC off: cost 0, next temp moves toward outdoor
            nt = move_towards(temp, temperature)
            nc = cost
            if nt not in next_dp or nc < next_dp[nt]:
                next_dp[nt] = nc

            # 2) AC on and keep same: next temp = temp, cost b
            nt = temp
            nc = cost + b
            if nt not in next_dp or nc < next_dp[nt]:
                next_dp[nt] = nc

            # 3) AC on and increase by 1: next temp = temp + 1, cost a
            nt = temp + 1
            nc = cost + a
            if nt not in next_dp or nc < next_dp[nt]:
                next_dp[nt] = nc

            # 4) AC on and decrease by 1: next temp = temp - 1, cost a
            nt = temp - 1
            nc = cost + a
            if nt not in next_dp or nc < next_dp[nt]:
                next_dp[nt] = nc

        # move to minute i+1
        dp = next_dp

    # After processing minute n-1, dp are states at minute n (no passenger constraint at minute n)
    # The minimal cost overall is the minimum value in dp
    return min(dp.values())


# --- 간단한 테스트 (문제 예시) ---
if __name__ == "__main__":
    # example 1
    print(solution(28, 18, 26, 10, 8, [0,0,1,1,1,1,1]))  # expected 40
    # example 2
    print(solution(-10, -5, 5, 5, 1, [0,0,0,0,0,1,0]))   # expected 25
    # example 3
    print(solution(11, 8, 10, 10, 1, [0,1,1,1,1,1,1,0,0,0,1,1]))  # expected 20
    # example 4
    print(solution(11, 8, 10, 10, 100, [0,1,1,1,1,1,1,0,0,0,1,1]))  # expected 60
