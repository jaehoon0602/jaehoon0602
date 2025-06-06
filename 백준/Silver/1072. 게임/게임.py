def min_games_to_increase_win_rate(x, y):
    z = (y * 100) // x
    if z >= 99:
        return -1

    low, high = 1, 1000000000
    result = -1

    while low <= high:
        mid = (low + high) // 2
        new_z = ((y + mid) * 100) // (x + mid)
        if new_z > z:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

# 입력 처리
if __name__ == "__main__":
    import sys
    x, y = map(int, sys.stdin.readline().split())
    print(min_games_to_increase_win_rate(x, y))
