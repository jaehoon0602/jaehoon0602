def solution(a, b):
    # 각 달의 일 수 (윤년이므로 2월은 29일)
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 요일 리스트: 일요일부터 시작
    weekdays = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    # 1월 1일부터 a월 b일까지 며칠이 지났는지 계산
    total_days = sum(month_days[:a-1]) + b - 1
    
    # 요일 계산
    return weekdays[total_days % 7]
