def solution(name, yearning, photo):
    # 이름과 그리움 점수를 매핑
    score_dict = {n: y for n, y in zip(name, yearning)}
    
    # 결과 리스트 초기화
    result = []
    
    # 각 사진마다 추억 점수 계산
    for people in photo:
        total = sum(score_dict.get(person, 0) for person in people)
        result.append(total)
    
    return result
