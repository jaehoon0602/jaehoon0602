def solution(video_len, pos, op_start, op_end, commands):
    def to_seconds(time_str):
        mm, ss = map(int, time_str.split(":"))
        return mm * 60 + ss
    
    def to_time_str(seconds):
        mm = seconds // 60
        ss = seconds % 60
        return f"{str(mm).zfill(2)}:{str(ss).zfill(2)}"
    
    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)
    
    # 처음 위치가 오프닝 구간이면 점프
    if op_start <= pos <= op_end:
        pos = op_end
    
    for cmd in commands:
        if cmd == "prev":
            pos = max(0, pos - 10)
        elif cmd == "next":
            pos = min(video_len, pos + 10)
        
        # 명령 실행 후 오프닝 구간 확인
        if op_start <= pos <= op_end:
            pos = op_end
    
    return to_time_str(pos)
