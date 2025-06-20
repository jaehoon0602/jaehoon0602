def solution(sizes):
    max_width = 0
    max_height = 0
    
    for w, h in sizes:
        longer = max(w, h)
        shorter = min(w, h)
        max_width = max(max_width, longer)
        max_height = max(max_height, shorter)
        
    return max_width * max_height
