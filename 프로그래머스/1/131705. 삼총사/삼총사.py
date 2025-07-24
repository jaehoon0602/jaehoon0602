from itertools import combinations

def solution(number):
    count = 0
    # 3명의 학생을 뽑는 모든 조합을 확인
    for trio in combinations(number, 3):
        if sum(trio) == 0:
            count += 1
    return count
