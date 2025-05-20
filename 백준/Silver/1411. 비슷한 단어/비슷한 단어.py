def normalize(word):
    mapping = {}
    pattern = []
    next_code = 0
    for ch in word:
        if ch not in mapping:
            mapping[ch] = next_code
            next_code += 1
        pattern.append(mapping[ch])
    return tuple(pattern)

n = int(input())
words = [input().strip() for _ in range(n)]

# 패턴 그룹별로 개수 세기
from collections import defaultdict

pattern_counts = defaultdict(int)

for word in words:
    norm = normalize(word)
    pattern_counts[norm] += 1

# 각 패턴 그룹에서 가능한 쌍의 수 구하기: nC2 = n*(n-1)//2
result = 0
for count in pattern_counts.values():
    if count >= 2:
        result += count * (count - 1) // 2

print(result)
