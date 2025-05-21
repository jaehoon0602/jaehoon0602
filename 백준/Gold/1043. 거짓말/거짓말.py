def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a_root = find(parent, a)
    b_root = find(parent, b)
    if a_root != b_root:
        parent[b_root] = a_root

# 입력 처리
n, m = map(int, input().split())
input_data = list(map(int, input().split()))
truth_known = input_data[1:] if input_data[0] > 0 else []

parties = []
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    parties.append(party)

# 유니온 파인드 초기화
parent = [i for i in range(n + 1)]

# 모든 파티의 사람들을 하나의 집합으로 묶기
for party in parties:
    for i in range(len(party) - 1):
        union(parent, party[i], party[i + 1])

# 진실을 아는 사람들의 루트 집합
truth_roots = set(find(parent, person) for person in truth_known)

# 과장해서 이야기할 수 있는 파티 수 계산
count = 0
for party in parties:
    if all(find(parent, person) not in truth_roots for person in party):
        count += 1

print(count)
