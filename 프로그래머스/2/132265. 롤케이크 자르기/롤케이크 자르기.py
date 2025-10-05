def solution(topping):
    from collections import defaultdict

    left = set()
    right = defaultdict(int)
    result = 0

    # 오른쪽 부분 토핑 종류 세기
    for t in topping:
        right[t] += 1

    # 한 조각씩 이동하면서 비교
    for i in range(len(topping) - 1):
        t = topping[i]
        left.add(t)
        right[t] -= 1
        if right[t] == 0:
            del right[t]
        # 토핑 종류 개수가 같을 때 카운트 증가
        if len(left) == len(right):
            result += 1

    return result
