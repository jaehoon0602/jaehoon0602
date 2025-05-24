import sys
sys.setrecursionlimit(1000)

def dfs(node):
    times = []
    for child in tree[node]:
        times.append(dfs(child))
    
    times.sort(reverse=True)
    
    max_time = 0
    for i, t in enumerate(times):
        max_time = max(max_time, t + i + 1)
    return max_time

# 입력
N = int(input())
boss = list(map(int, input().split()))

# 트리 구성
tree = [[] for _ in range(N)]
for i in range(1, N):
    tree[boss[i]].append(i)

# 결과 출력
print(dfs(0))
