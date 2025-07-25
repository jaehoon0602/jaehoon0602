def solution(num, k):
    num_str = str(num)
    k_str = str(k)
    
    if k_str in num_str:
        return num_str.index(k_str) + 1  # 1부터 시작하는 자리 수
    else:
        return -1
