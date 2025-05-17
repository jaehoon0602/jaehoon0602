N = int(input())
original = N
count = 0

while True:
    tens = N // 10
    ones = N % 10
    digit_sum = tens + ones
    N = (ones * 10) + (digit_sum % 10)
    count += 1
    if N == original:
        break

print(count)
