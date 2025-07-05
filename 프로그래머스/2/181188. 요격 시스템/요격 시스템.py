def solution(targets):
    # 끝점 기준으로 정렬
    targets.sort(key=lambda x: x[1])
    
    count = 0
    last_shot = -1  # 마지막으로 요격 미사일을 발사한 위치 (실수 좌표)

    for s, e in targets:
        # 현재 요격 위치가 이 구간에 속하지 않으면 새로 요격
        if not (s < last_shot < e):
            # 새로운 요격 위치: e보다 조금 작은 실수 위치
            last_shot = e - 0.5
            count += 1

    return count
