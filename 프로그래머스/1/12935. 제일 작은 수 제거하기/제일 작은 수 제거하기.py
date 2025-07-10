def solution(arr):
    # 배열에 원소가 하나뿐이라면 [-1] 리턴
    if len(arr) == 1:
        return [-1]
    
    # 가장 작은 값 구하기
    min_val = min(arr)
    
    # 가장 작은 값 제거한 새 배열 리턴
    return [x for x in arr if x != min_val]
