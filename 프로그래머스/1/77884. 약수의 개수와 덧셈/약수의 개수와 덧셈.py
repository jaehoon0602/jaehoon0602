def solution(left, right):
    total = 0
    for num in range(left, right + 1):
        # 제곱수인 경우 약수의 개수가 홀수
        if int(num**0.5) == num**0.5:
            total -= num
        else:
            total += num
    return total
