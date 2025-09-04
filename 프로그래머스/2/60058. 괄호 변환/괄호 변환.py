def is_correct(s: str) -> bool:
    """올바른 괄호 문자열인지 확인"""
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


def split_balanced(s: str):
    """균형잡힌 문자열 u, v로 분리"""
    left = right = 0
    for i, ch in enumerate(s):
        if ch == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return s[:i+1], s[i+1:]
    return s, ""


def transform(w: str) -> str:
    # 1. 입력이 빈 문자열이면 빈 문자열 반환
    if not w:
        return ""

    # 2. 문자열 w를 균형잡힌 u, v로 분리
    u, v = split_balanced(w)

    # 3. u가 올바른 괄호 문자열이면 v를 재귀적으로 처리 후 이어붙임
    if is_correct(u):
        return u + transform(v)

    # 4. u가 올바르지 않으면 규칙에 따라 새로운 문자열 생성
    else:
        # 4-1, 4-2, 4-3
        new_str = "(" + transform(v) + ")"
        # 4-4: u의 첫/마지막 제거 후 괄호 방향 뒤집기
        flipped = ''.join('(' if ch == ')' else ')' for ch in u[1:-1])
        return new_str + flipped


def solution(p: str) -> str:
    return transform(p)


# 실행 예시
print(solution("(()())()"))  # "(()())()"
print(solution(")("))        # "()"
print(solution("()))((()"))  # "()(())()"
