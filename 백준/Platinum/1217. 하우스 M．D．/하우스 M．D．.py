import sys
sys.setrecursionlimit(10**6)

def index(x):
    return x * 2 if x > 0 else -2 * x + 1

def opp(x):
    return x ^ 1

def dfs(u, adj, visited, stack):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v, adj, visited, stack)
    stack.append(u)

def reverse_dfs(u, radj, visited, label, comp_id):
    visited[u] = True
    label[u] = comp_id
    for v in radj[u]:
        if not visited[v]:
            reverse_dfs(v, radj, visited, label, comp_id)

def solve_2sat(N, M, clauses):
    size = 2 * M + 2
    adj = [[] for _ in range(size)]
    radj = [[] for _ in range(size)]

    for a, b in clauses:
        a_idx = index(a)
        b_idx = index(b)
        adj[opp(a_idx)].append(b_idx)
        adj[opp(b_idx)].append(a_idx)
        radj[b_idx].append(opp(a_idx))
        radj[a_idx].append(opp(b_idx))

    visited = [False] * size
    stack = []
    for i in range(2, size):
        if not visited[i]:
            dfs(i, adj, visited, stack)

    visited = [False] * size
    label = [0] * size
    comp_id = 0
    while stack:
        u = stack.pop()
        if not visited[u]:
            reverse_dfs(u, radj, visited, label, comp_id)
            comp_id += 1

    for i in range(1, M + 1):
        if label[2 * i] == label[2 * i + 1]:
            return 0
    return 1

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    results = []
    while True:
        N = int(data[idx])
        M = int(data[idx + 1])
        idx += 2
        if N == 0 and M == 0:
            break
        clauses = []
        for _ in range(N):
            a = int(data[idx])
            b = int(data[idx + 1])
            clauses.append((a, b))
            idx += 2
        results.append(str(solve_2sat(N, M, clauses)))
    print('\n'.join(results))

if __name__ == "__main__":
    main()
