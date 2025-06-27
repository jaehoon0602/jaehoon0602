def solution(n, m, section):
    answer = 0
    last_painted = 0  # 마지막으로 칠한 구역의 끝 번호

    for s in section:
        if s > last_painted:
            answer += 1
            last_painted = s + m - 1  # 현재 구역부터 롤러 길이만큼 칠함

    return answer
