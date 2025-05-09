def count_less_equal(mid, N):
    count = 0
    for i in range(1, N + 1):
        count += min(mid // i, N)
    return count

def find_kth_number(N, k):
    left, right = 1, N * N
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if count_less_equal(mid, N) >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

# 입력 처리
N = int(input())
k = int(input())

# 결과 출력
print(find_kth_number(N, k))
