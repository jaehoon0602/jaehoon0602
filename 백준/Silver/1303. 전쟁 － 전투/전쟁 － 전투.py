from collections import deque

def bfs(x, y, team):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[ny][nx] and battlefield[ny][nx] == team:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                    count += 1
    return count

# 입력
N, M = map(int, input().split())
battlefield = [list(input().strip()) for _ in range(M)]
visited = [[False]*N for _ in range(M)]

white_power = 0
blue_power = 0

for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            team = battlefield[y][x]
            group_size = bfs(x, y, team)
            power = group_size ** 2
            if team == 'W':
                white_power += power
            else:
                blue_power += power

print(white_power, blue_power)
