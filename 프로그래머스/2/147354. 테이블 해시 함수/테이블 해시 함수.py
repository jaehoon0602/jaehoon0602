def solution(data, col, row_begin, row_end):
    """
    주어진 규칙에 따라 테이블의 해시 값을 계산합니다.

    Args:
        data (list[list[int]]): 테이블의 데이터 (튜플들의 리스트).
        col (int): 정렬의 주 기준이 될 컬럼의 번호 (1-based).
        row_begin (int): 해시 값 계산에 포함될 시작 행 번호 (1-based, inclusive).
        row_end (int): 해시 값 계산에 포함될 종료 행 번호 (1-based, inclusive).

    Returns:
        int: 계산된 해시 값 (bitwise XOR의 누적).
    """

    # 1. 정렬
    # - 주 기준: col-1 번째 컬럼 값으로 오름차순 정렬 (key[col-1])
    # - 부 기준 (값이 동일한 경우): 0 번째 컬럼 값 (기본키)으로 내림차순 정렬 (-key[0] 사용)
    # col은 1-based, 파이썬 인덱스는 0-based이므로 col-1을 사용합니다.
    sorted_data = sorted(data, key=lambda row: (row[col - 1], -row[0]))

    hash_value = 0

    # row_begin과 row_end는 1-based 인덱스입니다.
    # 이를 0-based 인덱스로 변환하면 (row_begin - 1) 부터 (row_end - 1)까지가 됩니다.
    # 반복문에서는 i가 1-based 행 번호를 나타내도록 합니다.
    for i in range(row_begin, row_end + 1):
        # 2. S_i 계산
        # 현재 튜플은 sorted_data의 i-1 인덱스에 위치합니다.
        current_tuple = sorted_data[i - 1]
        S_i = 0
        
        # 튜플의 각 컬럼 값 col_val에 대해 i로 나눈 나머지들의 합을 계산합니다.
        # i는 현재 행 번호(1-based)이며, 이 값으로 나눕니다.
        for col_val in current_tuple:
            S_i += (col_val % i)
        
        # 3. XOR 누적
        # S_i 값을 누적하여 bitwise XOR 연산합니다.
        hash_value ^= S_i

    return hash_value