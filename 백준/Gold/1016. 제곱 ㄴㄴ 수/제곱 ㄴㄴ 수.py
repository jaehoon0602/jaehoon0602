import math

min_val, max_val = map(int, input().split())
size = max_val - min_val + 1
is_square_free = [True] * size

for i in range(2, int(math.sqrt(max_val)) + 1):
    square = i * i
    # 최소 범위 내에서 square의 배수 찾기
    start = ((min_val + square - 1) // square) * square
    for j in range(start, max_val + 1, square):
        is_square_free[j - min_val] = False

print(is_square_free.count(True))
