def solution(keymap, targets):
    # 각 문자의 최소 입력 횟수를 저장할 딕셔너리
    min_presses = {}

    # keymap을 탐색하면서 각 문자에 대한 최소 입력 횟수 기록
    for key_index, key in enumerate(keymap):
        for idx, char in enumerate(key):
            # 누른 횟수는 인덱스 + 1 (1부터 시작)
            press_count = idx + 1
            if char not in min_presses or press_count < min_presses[char]:
                min_presses[char] = press_count

    # 결과 리스트
    result = []

    # 각 target 문자열에 대해 최소 입력 횟수를 계산
    for word in targets:
        total = 0
        for char in word:
            if char not in min_presses:
                total = -1
                break
            total += min_presses[char]
        result.append(total)

    return result
