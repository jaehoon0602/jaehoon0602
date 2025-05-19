from collections import Counter

def solve(A):
    N = len(A)
    counter = Counter(A)
    path = []
    result = []

    def backtrack():
        if len(path) == N:
            result.append(path[:])
            return True  # 정답 찾았으니 종료

        for num in sorted(counter.keys()):
            if counter[num] == 0:
                continue
            if path and path[-1] + 1 == num:
                continue  # 연속된 숫자 안됨

            path.append(num)
            counter[num] -= 1
            if backtrack():
                return True
            counter[num] += 1
            path.pop()

        return False

    backtrack()
    return result[0] if result else []

# 입력
N = int(input())
A = list(map(int, input().split()))

# 실행
answer = solve(A)
print(' '.join(map(str, answer)))
