def solution(food):
    result = ''
    
    # 1번 음식부터 마지막 음식까지 반복
    for i in range(1, len(food)):
        # 각 음식의 절반만큼 문자열로 추가 (두 선수에게 나눠주기 위함)
        result += str(i) * (food[i] // 2)
    
    # 완성된 음식 배치를 좌측 + 물 + 우측(역순)으로 반환
    return result + '0' + result[::-1]
