from collections import Counter

def solution(X, Y):
    # 각 숫자의 개수를 세기
    count_x = Counter(X)
    count_y = Counter(Y)

    # 결과를 담을 리스트
    result = []

    # 9부터 0까지 숫자를 확인하며 공통으로 몇 개 있는지 확인
    for digit in map(str, range(9, -1, -1)):
        if digit in count_x and digit in count_y:
            common_count = min(count_x[digit], count_y[digit])
            result.append(digit * common_count)

    # 결과가 없으면 -1
    if not result:
        return "-1"

    answer = ''.join(result)

    # 0으로만 구성되어 있으면 0
    if answer[0] == '0':
        return "0"

    return answer
