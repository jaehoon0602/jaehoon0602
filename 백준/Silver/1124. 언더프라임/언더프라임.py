def get_primes_upto(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def count_prime_factors_up_to(n):
    count = [0] * (n + 1)
    for i in range(2, n + 1):
        if count[i] == 0:  # i is prime
            for j in range(i, n + 1, i):
                temp = j
                while temp % i == 0:
                    count[j] += 1
                    temp //= i
    return count

def count_underprimes(A, B):
    is_prime = get_primes_upto(100000)
    prime_factors = count_prime_factors_up_to(100000)
    
    result = 0
    for i in range(A, B + 1):
        if is_prime[prime_factors[i]]:
            result += 1
    return result

# 예제 입력
A, B = map(int, input().split())
print(count_underprimes(A, B))
