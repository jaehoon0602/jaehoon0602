def solution(n):
    sieve = [True] * (n+1)  # True로 초기화
    sieve[0], sieve[1] = False, False  # 0과 1은 소수가 아님
    
    # √n까지만 검사
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            # i의 배수들을 모두 False로 처리
            for j in range(i*i, n+1, i):
                sieve[j] = False
    
    return sum(sieve)  # True(소수)의 개수 합산
