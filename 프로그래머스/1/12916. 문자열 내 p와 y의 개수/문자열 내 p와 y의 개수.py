def solution(s):
    s = s.lower()  # 모두 소문자로 변환
    return s.count('p') == s.count('y')
