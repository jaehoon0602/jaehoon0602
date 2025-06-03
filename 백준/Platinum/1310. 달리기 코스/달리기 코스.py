import sys
import math
input = sys.stdin.readline

def dist2(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def ccw(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1])

def convex_hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def rotating_calipers(hull):
    n = len(hull)
    if n == 2:
        return dist2(hull[0], hull[1])
    max_dist = 0
    j = 1
    for i in range(n):
        next_i = (i + 1) % n
        while True:
            next_j = (j + 1) % n
            cur = abs(ccw(hull[i], hull[next_i], hull[next_j]))
            prev = abs(ccw(hull[i], hull[next_i], hull[j]))
            if cur > prev:
                j = next_j
            else:
                break
        max_dist = max(max_dist, dist2(hull[i], hull[j]))
    return max_dist

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(0)
elif N == 2:
    print(dist2(points[0], points[1]))
else:
    hull = convex_hull(points)
    print(rotating_calipers(hull))
