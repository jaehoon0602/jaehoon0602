from collections import deque

def min_jumps_to_target(N, stones, start, end):
    visited = [False] * N
    queue = deque()
    
    start -= 1  # 인덱스로 변환
    end -= 1

    queue.append((start, 0))  # (현재 위치, 점프 횟수)
    visited[start] = True

    while queue:
        pos, jumps = queue.popleft()
        
        step = stones[pos]
        for k in range(1, N):  # 최대 N-1배수까지 가능 (안전하게)
            forward = pos + step * k
            backward = pos - step * k

            if forward >= N and backward < 0:
                break

            if forward < N and not visited[forward]:
                if forward == end:
                    return jumps + 1
                visited[forward] = True
                queue.append((forward, jumps + 1))

            if backward >= 0 and not visited[backward]:
                if backward == end:
                    return jumps + 1
                visited[backward] = True
                queue.append((backward, jumps + 1))

    return -1  # 도달 불가

# 입력 처리
N = int(input())
stones = list(map(int, input().split()))
a, b = map(int, input().split())

# 결과 출력
print(min_jumps_to_target(N, stones, a, b))
