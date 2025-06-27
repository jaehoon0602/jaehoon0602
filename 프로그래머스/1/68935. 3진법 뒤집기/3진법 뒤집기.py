def solution(n):
    # 1. 10진법 정수를 3진법 문자열로 변환
    ternary = ''
    while n > 0:
        n, r = divmod(n, 3)
        ternary += str(r)  # 뒤집으면서 동시에 저장

    # 2. 이미 뒤집힌 3진법 문자열을 10진법 정수로 변환
    return int(ternary, 3)
