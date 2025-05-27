from itertools import combinations
from bisect import bisect_left, bisect_right

def get_subsequence_sums(arr):
    sums = []
    n = len(arr)
    for i in range(1, n + 1):
        for comb in combinations(arr, i):
            sums.append(sum(comb))
    return sums

def count_subsequence_sums(N, S, nums):
    mid = N // 2
    left = nums[:mid]
    right = nums[mid:]

    left_sums = get_subsequence_sums(left)
    right_sums = get_subsequence_sums(right)

    # 오른쪽 합 리스트 정렬
    right_sums.sort()

    count = 0
    for l in left_sums:
        target = S - l
        count += bisect_right(right_sums, target) - bisect_left(right_sums, target)

    # 오른쪽만 단독으로 만들 수 있는 S도 포함해야 하므로 왼쪽 공집합 고려
    count += right_sums.count(S)
    count += left_sums.count(S)

    return count

# 입력 처리
N, S = map(int, input().split())
nums = list(map(int, input().split()))

print(count_subsequence_sums(N, S, nums))
