def solution(n, lost, reserve):
    # 여벌이 있지만 도난당한 학생을 먼저 처리 (자기 체육복 사용)
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
    
    return n - len(lost_set)
