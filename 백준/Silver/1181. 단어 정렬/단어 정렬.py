# 입력 받기
n = int(input())
words = [input().strip() for _ in range(n)]

# 중복 제거
unique_words = set(words)

# 정렬
sorted_words = sorted(unique_words, key=lambda x: (len(x), x))

# 출력
for word in sorted_words:
    print(word)
