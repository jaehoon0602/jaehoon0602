def solution(answers):
    # 수포자들의 찍는 패턴 정의
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자의 점수 저장
    scores = [0, 0, 0]
    
    # 전체 문제 순회하며 정답 비교
    for i, answer in enumerate(answers):
        if answer == person1[i % len(person1)]:
            scores[0] += 1
        if answer == person2[i % len(person2)]:
            scores[1] += 1
        if answer == person3[i % len(person3)]:
            scores[2] += 1

    # 최고 점수 구함
    max_score = max(scores)

    # 최고 점수를 받은 사람들(1-indexed) 반환
    return [i + 1 for i, score in enumerate(scores) if score == max_score]
