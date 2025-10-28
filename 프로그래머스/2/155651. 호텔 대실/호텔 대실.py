import heapq

def solution(book_time):
    # 문자열 "HH:MM"을 분 단위로 변환하는 함수
    def to_minutes(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    # 예약 시간(시작, 끝)을 분 단위로 변환
    times = [(to_minutes(start), to_minutes(end)) for start, end in book_time]
    
    # 시작 시각 기준 정렬
    times.sort()

    # 최소 힙 (각 방이 언제 비워지는지 저장)
    rooms = []

    for start, end in times:
        # 청소 시간 10분 추가
        available_time = end + 10

        # 만약 현재 시작 시간이 가장 빨리 비워지는 방의 시간 이후라면 → 그 방 재사용 가능
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)  # 가장 빨리 비워지는 방 제거

        heapq.heappush(rooms, available_time)  # 새로 배정(또는 업데이트)

    # 방의 개수 = 필요한 최소 객실 수
    return len(rooms)
