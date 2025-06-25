def solution(a, b, n):
    answer = 0
    while n >= a:
        exchanged = (n // a) * b  # 새로 받은 콜라 수
        answer += exchanged
        n = (n % a) + exchanged  # 남은 병 + 새 콜라 마신 병
    return answer
