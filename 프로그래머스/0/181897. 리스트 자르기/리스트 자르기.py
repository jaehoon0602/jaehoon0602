def solution(n, slicer, num_list):
    a, b, c = slicer
    
    if n == 1:
        return num_list[:b+1]       # 0번 인덱스부터 b번 인덱스까지
    elif n == 2:
        return num_list[a:]         # a번 인덱스부터 끝까지
    elif n == 3:
        return num_list[a:b+1]      # a번 인덱스부터 b번 인덱스까지
    elif n == 4:
        return num_list[a:b+1:c]    # a번 인덱스부터 b번 인덱스까지 c 간격으로
