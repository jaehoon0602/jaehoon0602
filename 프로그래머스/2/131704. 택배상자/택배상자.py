def solution(order):
    stack = []
    idx = 0  # 현재 실어야 할 박스 인덱스
    n = len(order)

    for box in range(1, n+1):  # 벨트에서 1~n까지 상자가 순서대로 옴
        stack.append(box)  # 일단 보조 컨테이너에 저장
        # 보조 컨테이너의 top이 현재 실어야 할 상자와 같으면 계속 꺼냄
        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1
            if idx == n:  # 모든 상자를 실었다면 종료
                return n

    return idx
