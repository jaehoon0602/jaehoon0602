from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])

    visited = [[False] * m for _ in range(n)]

    # 시작 위치 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            if board[i][j] == 'G':
                goal = (i, j)

    # 상하좌우 방향벡터
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque()
    queue.append((*start, 0))
    visited[start[0]][start[1]] = True

    while queue:
        x, y, cnt = queue.popleft()

        if (x, y) == goal:
            return cnt

        for dx, dy in directions:
            nx, ny = x, y
            # 미끄러지기
            while True:
                tx, ty = nx + dx, ny + dy
                if 0 <= tx < n and 0 <= ty < m and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                else:
                    break
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))

    return -1
