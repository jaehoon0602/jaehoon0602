def solution(n, l, r):
    def count_ones(n, l, r):
        if n == 0:
            # n=0이면 문자열은 "1"
            return 1 if l <= 1 <= r else 0

        length = 5 ** n
        part_len = length // 5

        result = 0
        for i in range(5):
            start = i * part_len + 1
            end = (i + 1) * part_len

            # 구간이 겹치지 않으면 건너뜀
            if r < start or l > end:
                continue

            # 가운데 구간(i == 2)은 무조건 0
            if i == 2:
                continue

            # 완전히 포함되면 1의 개수는 4^(n-1)
            if l <= start and end <= r:
                result += 4 ** (n - 1)
            else:
                # 부분적으로 겹치면 재귀적으로 탐색
                nl = max(l, start) - start + 1
                nr = min(r, end) - start + 1
                result += count_ones(n - 1, nl, nr)

        return result

    return count_ones(n, l, r)
