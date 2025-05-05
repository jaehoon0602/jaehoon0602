from collections import Counter

# 입력
n = int(input())
books = [input().strip() for _ in range(n)]

# 책 제목 빈도수 세기
counter = Counter(books)

# 가장 많이 팔린 책의 판매 수
max_count = max(counter.values())

# 가장 많이 팔린 책들 중에서 사전 순으로 가장 앞선 제목 찾기
most_sold_books = [title for title, count in counter.items() if count == max_count]
most_sold_books.sort()

# 출력
print(most_sold_books[0])
