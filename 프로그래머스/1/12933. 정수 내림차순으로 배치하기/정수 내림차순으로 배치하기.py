def solution(n):
    # 1. 정수를 문자열로 변환
    digits = str(n)
    
    # 2. 각 자릿수를 큰 순서로 정렬
    sorted_digits = sorted(digits, reverse=True)
    
    # 3. 정렬된 숫자를 이어붙여 문자열로 만들고 다시 정수로 변환
    return int(''.join(sorted_digits))

# 예시 실행
print(solution(118372))  # 873211
