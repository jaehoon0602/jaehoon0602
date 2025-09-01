def solution(friends, gifts):
    n = len(friends)
    idx = {name: i for i, name in enumerate(friends)}  # 이름 → 인덱스 매핑
    
    # 선물 주고받은 횟수 기록
    give_matrix = [[0] * n for _ in range(n)]
    given = [0] * n
    received = [0] * n
    
    for g in gifts:
        a, b = g.split()
        ai, bi = idx[a], idx[b]
        give_matrix[ai][bi] += 1
        given[ai] += 1
        received[bi] += 1
    
    # 선물 지수
    gift_index = [given[i] - received[i] for i in range(n)]
    
    # 다음 달 받을 선물 수
    next_receive = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):  # i, j 쌍만 확인
            if give_matrix[i][j] > give_matrix[j][i]:
                next_receive[i] += 1
            elif give_matrix[i][j] < give_matrix[j][i]:
                next_receive[j] += 1
            else:  # 같을 경우 선물 지수 비교
                if gift_index[i] > gift_index[j]:
                    next_receive[i] += 1
                elif gift_index[i] < gift_index[j]:
                    next_receive[j] += 1
                # 같으면 아무도 받지 않음
    
    return max(next_receive)
