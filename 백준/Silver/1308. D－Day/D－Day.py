from datetime import date

# 입력
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

# 날짜 객체 생성
start = date(y1, m1, d1)
end = date(y2, m2, d2)

# 1000년 이상 차이나는 경우 처리
if (y2 - y1 > 1000) or (y2 - y1 == 1000 and (m2, d2) >= (m1, d1)):
    print("gg")
else:
    days_left = (end - start).days
    print(f"D-{days_left}")
