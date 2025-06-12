def solution(n, w, num):
    count = 1  # 본인 상자 포함
    row = (num-1) // w
    if row % 2 == 0:  # 홀수층(0부터 시작)
        col = (num-1) % w
    else:  # 짝수층
        col = w - 1 - (num-1) % w

    # 위층 탐색
    for r in range(row+1, (n-1)//w + 1):
        if r % 2 == 0:
            boxNum = r * w + col + 1
        else:
            boxNum = (r+1) * w - col
        if boxNum > n:
            continue
        count += 1
    return count
