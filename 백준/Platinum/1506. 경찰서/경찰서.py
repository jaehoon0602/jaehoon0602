import sys
sys.setrecursionlimit(10000)

N = int(input())
costs = list(map(int, input().split()))
graph = [[] for _ in range(N)]

# 그래프 입력
for i in range(N):
    line = input()
    for j in range(N):
        if line[j] == '1':
            graph[i].append(j)

# Tarjan's Algorithm for SCC
index = 0
stack = []
indices = [-1] * N
lowlink = [0] * N
on_stack = [False] * N
sccs = []

def strongconnect(v):
    global index
    indices[v] = index
    lowlink[v] = index
    index += 1
    stack.append(v)
    on_stack[v] = True

    for w in graph[v]:
        if indices[w] == -1:
            strongconnect(w)
            lowlink[v] = min(lowlink[v], lowlink[w])
        elif on_stack[w]:
            lowlink[v] = min(lowlink[v], indices[w])

    if lowlink[v] == indices[v]:
        scc = []
        while True:
            w = stack.pop()
            on_stack[w] = False
            scc.append(w)
            if w == v:
                break
        sccs.append(scc)

# Run Tarjan
for v in range(N):
    if indices[v] == -1:
        strongconnect(v)

# 각 SCC마다 최소 비용 계산
total_cost = 0
for scc in sccs:
    min_cost = min(costs[v] for v in scc)
    total_cost += min_cost

print(total_cost)
