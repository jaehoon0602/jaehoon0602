import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def is_bipartite(V, adj):
    color = [0] * (V + 1)  # 0: 미방문, 1: 빨강, -1: 파랑

    for start in range(1, V + 1):
        if color[start] != 0:
            continue

        queue = deque([start])
        color[start] = 1  # 첫 시작은 빨강

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = -color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
    return True

K = int(input())
results = []

for _ in range(K):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    results.append("YES" if is_bipartite(V, adj) else "NO")

print('\n'.join(results))
