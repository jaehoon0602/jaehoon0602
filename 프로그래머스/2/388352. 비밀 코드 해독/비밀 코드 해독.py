from itertools import combinations

def solution(n, q, ans):
    # 가능한 모든 비밀 코드 조합 생성
    candidates = list(combinations(range(1, n+1), 5))
    
    count = 0
    for code in candidates:
        valid = True
        for attempt, response in zip(q, ans):
            # 비밀 코드와 입력한 시도의 공통된 숫자 개수
            common = len(set(code) & set(attempt))
            if common != response:
                valid = False
                break
        if valid:
            count += 1
    return count
