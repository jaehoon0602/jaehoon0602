def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s

def seconds_to_time(seconds):
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

# 입력 받기
current_time = input().strip()
start_time = input().strip()

# 초로 변환
current_sec = time_to_seconds(current_time)
start_sec = time_to_seconds(start_time)

# 남은 시간 계산 (24시간을 기준으로)
if start_sec >= current_sec:
    remaining_sec = start_sec - current_sec
else:
    remaining_sec = (24 * 3600 - current_sec) + start_sec

# 출력
print(seconds_to_time(remaining_sec))
