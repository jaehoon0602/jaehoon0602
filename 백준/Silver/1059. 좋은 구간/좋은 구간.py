L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())

# n보다 작은 수 중 가장 큰 수를 left로
left = 0
right = 1001

for s in S:
    if s < n:
        left = max(left, s)
    elif s > n and right > s:
        right = s
    elif s == n:
        # n이 S에 포함되어 있으면 좋은 구간은 0개
        print(0)
        exit()

# 가능한 좋은 구간 [A, B]에서 n을 포함해야 하므로
# A <= n <= B 이어야 함
# A in [left+1, n], B in [n, right-1]
count = 0
for a in range(left + 1, n + 1):
    for b in range(n, right):
        if a < b:
            count += 1

print(count)
