def solution(babbling):
    pronounce = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        tmp = ''
        i = 0
        while i < len(word):
            matched = False
            for p in pronounce:
                if word[i:i+len(p)] == p and tmp != p:
                    tmp = p
                    i += len(p)
                    matched = True
                    break
            if not matched:
                break
        else:  # while문이 break 없이 끝난 경우 (전부 성공)
            count += 1
    return count
