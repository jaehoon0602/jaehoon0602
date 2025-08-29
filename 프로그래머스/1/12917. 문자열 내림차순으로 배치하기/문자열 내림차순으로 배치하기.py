def solution(s):
    return ''.join(sorted(s, reverse=True))

# 테스트
print(solution("Zbcdefg"))  # 결과: "gfedcbZ"
