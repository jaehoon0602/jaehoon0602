def min_repaint(board, x, y):
    w_start = 0  # W로 시작하는 체스판 기준
    b_start = 0  # B로 시작하는 체스판 기준

    for i in range(8):
        for j in range(8):
            current = board[x + i][y + j]
            # 짝수 합 (i + j): 시작 색과 같아야 함
            if (i + j) % 2 == 0:
                if current != 'W':
                    w_start += 1
                if current != 'B':
                    b_start += 1
            else:
                if current != 'B':
                    w_start += 1
                if current != 'W':
                    b_start += 1

    return min(w_start, b_start)

# 입력 처리
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

# 모든 가능한 8x8 영역을 검사
min_count = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        repaint = min_repaint(board, i, j)
        min_count = min(min_count, repaint)

print(min_count)
