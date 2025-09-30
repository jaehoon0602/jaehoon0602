from collections import Counter

def solution(k, tangerine):
    # 1. 귤 크기별 개수 세기
    counter = Counter(tangerine)
    
    # 2. 개수를 내림차순 정렬
    counts = sorted(counter.values(), reverse=True)
    
    answer = 0
    total = 0
    
    # 3. 많은 종류부터 담기
    for c in counts:
        total += c
        answer += 1
        if total >= k:  # k개 이상 채웠으면 멈춤
            break
            
    return answer
