def solution(numbers):
    result = set()
    length = len(numbers)
    
    for i in range(length):
        for j in range(i + 1, length):
            result.add(numbers[i] + numbers[j])
    
    return sorted(result)
