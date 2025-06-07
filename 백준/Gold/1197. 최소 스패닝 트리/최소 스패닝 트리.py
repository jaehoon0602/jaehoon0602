import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def kruskal(v, edges):
    parent = [i for i in range(v + 1)]
    edges.sort(key=lambda x: x[2])  # 가중치 기준 정렬

    mst_weight = 0
    for a, b, cost in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            mst_weight += cost
    return mst_weight

def main():
    data = input().split()
    v = int(data[0])
    e = int(data[1])
    edges = []
    idx = 2
    for _ in range(e):
        a = int(data[idx])
        b = int(data[idx + 1])
        c = int(data[idx + 2])
        edges.append((a, b, c))
        idx += 3

    print(kruskal(v, edges))

if __name__ == "__main__":
    main()
