def solution(cards1, cards2, goal):
    idx1 = 0
    idx2 = 0
    
    for word in goal:
        if idx1 < len(cards1) and word == cards1[idx1]:
            idx1 += 1
        elif idx2 < len(cards2) and word == cards2[idx2]:
            idx2 += 1
        else:
            return "No"
    return "Yes"
