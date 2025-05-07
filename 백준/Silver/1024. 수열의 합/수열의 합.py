def find_sequence(N, L):
    for length in range(L, 101):  # 길이는 L부터 100까지 시도
        temp = N - (length * (length - 1)) // 2
        if temp < 0:
            continue  # 음수가 되면 그 다음 길이 시도
        if temp % length == 0:
            start = temp // length
            sequence = [start + i for i in range(length)]
            print(" ".join(map(str, sequence)))
            return
    print(-1)

# 입력
N, L = map(int, input().split())
find_sequence(N, L)
