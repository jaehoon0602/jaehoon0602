def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        # 현재 원소보다 작거나 같은 수는 스택에서 제거
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        
        # 스택이 비어있지 않다면, 스택 top이 뒷 큰수
        if stack:
            answer[i] = stack[-1]
        
        # 현재 숫자를 스택에 push
        stack.append(numbers[i])
    
    return answer
