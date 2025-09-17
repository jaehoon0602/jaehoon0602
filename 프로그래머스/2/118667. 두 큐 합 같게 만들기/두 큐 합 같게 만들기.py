from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    total = sum1 + sum2
    
    # 총합이 홀수면 불가능
    if total % 2 != 0:
        return -1
    
    target = total // 2
    cnt = 0
    limit = len(q1) * 3  # 최대 이동 가능 횟수 제한
    
    while cnt <= limit:
        if sum1 == target:
            return cnt
        if sum1 > target:  # q1에서 빼서 q2로
            x = q1.popleft()
            sum1 -= x
            sum2 += x
            q2.append(x)
        else:  # q2에서 빼서 q1으로
            x = q2.popleft()
            sum2 -= x
            sum1 += x
            q1.append(x)
        cnt += 1
    
    return -1
