def solution(array):
    max_value = max(array)         # 가장 큰 수 찾기
    max_index = array.index(max_value)  # 가장 큰 수의 인덱스 찾기
    return [max_value, max_index]
