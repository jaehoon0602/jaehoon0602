import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):  # x=0 제외, 나중에 대칭으로 처리됨
        # 바깥 원에 대한 최대 y
        max_y = int(math.floor(math.sqrt(r2**2 - x**2)))
        
        # 안쪽 원에 대한 최소 y
        min_y = 0
        if r1**2 - x**2 > 0:
            min_y = int(math.ceil(math.sqrt(r1**2 - x**2)))
        
        # 가능한 y 개수 더하기
        answer += (max_y - min_y + 1)
    
    # 사분면 4배 + y축과 x축 포함
    return answer * 4
