def solution(s):
    # 각 문자의 등장 횟수 세기
    from collections import Counter
    count = Counter(s)

    # 등장 횟수가 1인 문자만 추출
    one_time_chars = [char for char in count if count[char] == 1]

    # 사전 순 정렬
    one_time_chars.sort()

    # 리스트를 문자열로 변환하여 반환
    return ''.join(one_time_chars)
