def solution(arr, divisor):
    # divisor로 나누어 떨어지는 원소만 필터링
    result = [x for x in arr if x % divisor == 0]
    
    # 결과가 비었으면 [-1] 반환, 아니면 정렬된 결과 반환
    return sorted(result) if result else [-1]
