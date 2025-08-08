def solution(my_string):
    parts = my_string.split()
    result = int(parts[0])  # 첫 번째 숫자
    
    # 연산자는 홀수 인덱스, 숫자는 짝수 인덱스
    for i in range(1, len(parts), 2):
        op = parts[i]
        num = int(parts[i+1])
        
        if op == '+':
            result += num
        elif op == '-':
            result -= num
            
    return result
