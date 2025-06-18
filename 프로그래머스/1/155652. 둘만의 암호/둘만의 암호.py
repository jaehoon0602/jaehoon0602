def solution(s, skip, index):
    result = ''
    skip_set = set(skip)
    
    for char in s:
        count = 0
        next_char = ord(char)
        while count < index:
            next_char += 1
            if next_char > ord('z'):
                next_char = ord('a')
            if chr(next_char) not in skip_set:
                count += 1
        result += chr(next_char)
    
    return result
