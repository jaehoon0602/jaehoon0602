word = input()
min_word = None

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        part1 = word[:i][::-1]
        part2 = word[i:j][::-1]
        part3 = word[j:][::-1]
        combined = part1 + part2 + part3
        if min_word is None or combined < min_word:
            min_word = combined

print(min_word)
