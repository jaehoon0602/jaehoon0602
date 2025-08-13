def solution(n):
    # 혹시 문자열로 들어와도 int 변환
    n = int(n)
    return [int(ch) for ch in str(n)][::-1]

# 테스트
print(solution(12345))   # [5,4,3,2,1]
print(solution("9876"))  # [6,7,8,9]
