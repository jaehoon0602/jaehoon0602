N = int(input())
A = list(map(int, input().split()))

answer = -1
for k in range(N + 1):  # k: 참이라고 가정하는 문장의 수
    count = A.count(k)  # 실제로 "정확히 k개가 참이다"라고 말한 문장 개수
    if count == k:
        answer = k  # 조건 만족, 가능한 답. 가장 큰 값을 원하므로 계속 갱신.

print(answer)
