octal = input().strip()

# 0인 경우는 바로 출력
if octal == '0':
    print('0')
else:
    # 8진수 -> 10진수 -> 2진수
    binary = bin(int(octal, 8))[2:]
    print(binary)
