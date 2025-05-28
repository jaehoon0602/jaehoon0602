n = int(input())
nums = [input().strip() for _ in range(n)]
length = len(nums[0])

for k in range(1, length + 1):
    seen = set()
    for num in nums:
        seen.add(num[-k:])  # 뒤에서 k자리 추출
    if len(seen) == n:  # 중복이 없다면
        print(k)
        break
