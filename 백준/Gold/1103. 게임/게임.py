import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

dp = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
    if not (0 <= y < N and 0 <= x < M):
        return 0
    if board[y][x] == 'H':
        return 0
    if visited[y][x]:
        print(-1)
        exit()
    if dp[y][x] != 0:
        return dp[y][x]
    
    visited[y][x] = True
    move = int(board[y][x])
    max_cnt = 0
    for d in range(4):
        ny = y + dy[d]*move
        nx = x + dx[d]*move
        max_cnt = max(max_cnt, dfs(ny, nx) + 1)
    visited[y][x] = False
    dp[y][x] = max_cnt
    return dp[y][x]

print(dfs(0, 0))
