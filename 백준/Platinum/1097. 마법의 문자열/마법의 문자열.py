from itertools import permutations

def is_magic_string(s, K):
    L = len(s)
    count = 0
    for i in range(L):
        rotated = s[i:] + s[:i]
        if rotated == s:
            count += 1
    return count == K

def count_magic_permutations(words, K):
    result = 0
    for perm in permutations(words):
        combined = ''.join(perm)
        if is_magic_string(combined, K):
            result += 1
    return result

# 입력 처리
N = int(input())
words = [input().strip() for _ in range(N)]
K = int(input())

# 결과 출력
print(count_magic_permutations(words, K))
