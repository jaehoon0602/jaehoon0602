def solution(n, m, section):
    answer = 0
    idx = 0  # 현재 section 인덱스
    while idx < len(section):
        # section[idx]부터 롤러로 칠함
        paint_start = section[idx]
        paint_end = paint_start + m - 1
        answer += 1

        # 롤러로 칠한 범위 내의 구역들은 넘김
        while idx < len(section) and section[idx] <= paint_end:
            idx += 1
    return answer
