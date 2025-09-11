# -*- coding: utf-8 -*-
"""
k개의 상담 유형, n명의 멘토(각 유형별 최소 1명)를 분배하여
참가자들이 멘토와 상담을 시작하기까지 기다린 시간의 합을 최소로 하는 문제.

방법:
- 각 유형별로 할당되는 멘토 수의 모든 분할(composition)을 완전탐색한다.
  k <= 5, n <= 20 이므로 조합 수가 충분히 작아 가능한 방법.
- 각 유형에 대해 해당 유형 요청들만 따로 모아 다중 서버(멘토) FIFO 큐로 시뮬레이션하여
  그 유형에서 발생하는 전체 대기시간을 계산한다.
- 모든 유형 대기시간 합의 최솟값을 답으로 반환한다.

시뮬레이션(한 유형에 대해 m명의 멘토):
- idle_count = m, busy_heap = min-heap(서버가 비는 시각들)
- 참가자 요청을 도착시간 순으로 처리한다.
  - 도착시간 a보다 이전에 끝나는 상담(<= a)이 있으면 그 수만큼 서버를 idle로 만들고 pop한다.
  - idle 서버가 있으면 즉시 시작(대기 0), busy_heap에 a + duration 넣음
  - idle 서버가 없으면 가장 이른 종료 시간을 pop -> 그때까지 대기: wait = earliest - a
    시작시간 = earliest, 종료시간 = earliest + duration, push back.

시간복잡도: 분할 개수 * (전체 요청 수 log m) -> 충분히 빠름.
"""
from heapq import heappush, heappop
from itertools import combinations


def wait_time_for_type(requests, m):
    """주어진 유형의 요청(requests: list of (a,b) 정렬됨)과 멘토 수 m에 대해
    총 대기시간 합을 반환한다."""
    if m <= 0:
        return float('inf')
    # 초기 상태: m개의 유휴 서버
    idle = m
    busy = []  # min-heap of end times
    total_wait = 0
    for a, dur in requests:
        # 서버들 중 a 이전(<= a)에 끝나는 것들을 유휴로 돌린다
        while busy and busy[0] <= a:
            heappop(busy)
            idle += 1
        if idle > 0:
            # 즉시 시작
            idle -= 1
            heappush(busy, a + dur)
        else:
            # 모든 서버가 바쁨 -> 가장 먼저 끝나는 서버를 꺼내 해당 시각까지 대기
            earliest = heappop(busy)
            total_wait += (earliest - a)
            # 바로 상담 시작되어 earliest + dur 에 끝남
            heappush(busy, earliest + dur)
    return total_wait


def generate_compositions(n, k):
    """n을 k개의 양의 정수 합으로 분해하는 모든 조합을 생성한다.
    반환: generator of lists length k where sum == n and each >=1"""
    # choose k-1 cut positions among n-1 gaps
    for cuts in combinations(range(1, n), k-1):
        parts = []
        prev = 0
        for c in cuts:
            parts.append(c - prev)
            prev = c
        parts.append(n - prev)
        yield parts


def solution(k, n, reqs):
    # 유형별 요청 분리
    type_reqs = [[] for _ in range(k + 1)]  # 1-indexed types
    for a, b, c in reqs:
        type_reqs[c].append((a, b))
    # 각 리스트는 이미 a 기준으로 오름차순이라고 문제에서 보장

    best = float('inf')
    # 모든 분할을 시도
    for alloc in generate_compositions(n, k):
        total = 0
        # alloc는 길이 k, alloc[i]는 type (i+1) 에 할당된 멘토 수
        for i in range(k):
            req_list = type_reqs[i+1]
            if not req_list:
                # 요청이 없는 유형이라도 멘토는 최소 1명 필요하지만 대기시간은 0
                continue
            total += wait_time_for_type(req_list, alloc[i])
            if total >= best:
                break
        if total < best:
            best = total
    return best


if __name__ == '__main__':
    # 예제 테스트
    k = 3
    n = 5
    reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]
    print(solution(k, n, reqs))  # expect 25

    k2 = 2
    n2 = 3
    reqs2 = [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]
    print(solution(k2, n2, reqs2))  # expect 90
