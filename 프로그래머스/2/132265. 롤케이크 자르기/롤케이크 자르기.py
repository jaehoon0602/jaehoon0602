from collections import Counter

def solution(topping):
    answer = 0
    
    # 오른쪽 조각 전체 토핑 카운트
    right_counter = Counter(topping)
    left_counter = set()
    
    for t in topping:
        # 왼쪽으로 토핑 하나 이동
        left_counter.add(t)
        right_counter[t] -= 1
        if right_counter[t] == 0:
            del right_counter[t]
        
        # 공평하게 나눠졌는지 확인
        if len(left_counter) == len(right_counter):
            answer += 1
    
    return answer
