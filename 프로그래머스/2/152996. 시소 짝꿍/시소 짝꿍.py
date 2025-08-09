from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)
    
    # 가능한 비율들
    ratios = [(1, 1), (2, 3), (1, 2), (3, 4)]
    
    for w in sorted(count):  # 작은 무게부터
        # 같은 무게끼리의 짝꿍 (1:1)
        if count[w] > 1:
            answer += count[w] * (count[w] - 1) // 2
        
        # 다른 무게끼리의 짝꿍
        for a, b in ratios[1:]:  # (1,1)은 위에서 처리
            target = w * b / a
            if target in count:
                answer += count[w] * count[target]
    
        # 중복 방지: 다음 단계에서 세지 않도록 현재 w 제거
        count[w] = 0
    
    return answer
