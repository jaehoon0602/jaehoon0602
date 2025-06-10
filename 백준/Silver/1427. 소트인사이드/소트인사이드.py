N = input()  # 숫자를 문자열로 입력받음
sorted_digits = sorted(N, reverse=True)  # 내림차순 정렬
print(''.join(sorted_digits))  # 리스트를 문자열로 합쳐 출력
