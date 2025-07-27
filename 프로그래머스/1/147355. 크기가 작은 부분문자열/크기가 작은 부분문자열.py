def solution(t, p):
    p_len = len(p)
    p_val = int(p)
    count = 0

    for i in range(len(t) - p_len + 1):
        sub = t[i:i+p_len]  # 부분 문자열 추출
        if int(sub) <= p_val:
            count += 1

    return count
