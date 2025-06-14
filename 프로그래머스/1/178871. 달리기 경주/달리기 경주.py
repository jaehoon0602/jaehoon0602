def solution(players, callings):
    # 선수 이름 → 현재 인덱스
    player_to_index = {name: idx for idx, name in enumerate(players)}
    
    for call in callings:
        idx = player_to_index[call]       # 현재 선수의 인덱스
        front_player = players[idx - 1]   # 앞에 있는 선수 이름

        # 순위 swap
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        
        # 딕셔너리 업데이트
        player_to_index[call] -= 1
        player_to_index[front_player] += 1

    return players
