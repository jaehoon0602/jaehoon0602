def max_profit(N, C, W, trees):
    max_len = max(trees)
    answer = 0

    for target_len in range(1, max_len + 1):
        total = 0
        for tree in trees:
            if tree < target_len:
                continue
            num_piece = tree // target_len
            num_cut = (tree // target_len - 1)
            if tree % target_len != 0:
                num_cut += 1

            profit = (num_piece * target_len * W) - (num_cut * C)
            if profit > 0:
                total += profit

        answer = max(answer, total)
    
    return answer

# 예제 입력
N, C, W = map(int, input().split())
trees = [int(input()) for _ in range(N)]

# 결과 출력
print(max_profit(N, C, W, trees))
