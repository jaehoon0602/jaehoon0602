from collections import Counter

def solution(participant, completion):
    # 참가자와 완주자 명단의 이름 개수를 셈
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    
    # 참가자 명단에서 완주자 명단을 빼면 완주하지 못한 사람이 남음
    diff = p_counter - c_counter
    
    # 남은 한 명의 이름을 반환 (딕셔너리의 key 중 하나)
    return list(diff.keys())[0]
