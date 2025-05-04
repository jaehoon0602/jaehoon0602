import sys

input = sys.stdin.readline

# 입력
N = int(input())
A, B = map(int, input().split())

points = set()
for _ in range(N):
    x, y = map(int, input().split())
    points.add((x, y))

count = 0

for x, y in points:
    if (
        (x + A, y) in points and
        (x, y + B) in points and
        (x + A, y + B) in points
    ):
        count += 1

print(count)
