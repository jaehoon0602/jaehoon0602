def solution(todo_list, finished):
    result = []
    for i in range(len(todo_list)):
        if not finished[i]:   # 아직 안 끝난 경우
            result.append(todo_list[i])
    return result
