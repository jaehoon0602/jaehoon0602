def solution(m, n, startX, startY, balls):
    answer = []
    
    for a, b in balls:
        candidates = []
        
        # 1. 위쪽 반사 (y축 위로 반사)
        if not (startX == a and startY < b):  # 같은 세로선 위에서 목표 공 위쪽에 있는 경우 제외
            dist = (startX - a) ** 2 + (startY - (2*n - b)) ** 2
            candidates.append(dist)
        
        # 2. 아래쪽 반사
        if not (startX == a and startY > b):  # 같은 세로선 위에서 목표 공 아래쪽에 있는 경우 제외
            dist = (startX - a) ** 2 + (startY - (-b)) ** 2
            candidates.append(dist)
        
        # 3. 오른쪽 반사
        if not (startY == b and startX < a):  # 같은 가로선 위에서 목표 공 오른쪽에 있는 경우 제외
            dist = (startX - (2*m - a)) ** 2 + (startY - b) ** 2
            candidates.append(dist)
        
        # 4. 왼쪽 반사
        if not (startY == b and startX > a):  # 같은 가로선 위에서 목표 공 왼쪽에 있는 경우 제외
            dist = (startX - (-a)) ** 2 + (startY - b) ** 2
            candidates.append(dist)
        
        answer.append(min(candidates))
    
    return answer
