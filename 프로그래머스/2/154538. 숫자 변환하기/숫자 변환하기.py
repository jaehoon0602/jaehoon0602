from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))  # (현재 숫자, 연산 횟수)
    visited = set()
    visited.add(x)
    
    while queue:
        current, count = queue.popleft()
        
        if current == y:
            return count
        
        for next_num in (current + n, current * 2, current * 3):
            if next_num <= y and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, count + 1))
    
    return -1
