def solution(ingredient):
    stack = []
    count = 0
    
    for i in ingredient:
        stack.append(i)
        # 스택에 최소 4개가 있어야 햄버거 완성 가능
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            # 햄버거 재료 제거
            del stack[-4:]
            count += 1
            
    return count
