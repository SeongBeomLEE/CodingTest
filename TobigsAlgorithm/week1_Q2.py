def solution(x):
    word_list = list(x)
    next = ''
    result = []
    for w in word_list:
        if w != next:
            result.append(w)
            next = w
    return ''.join(result)

word = input()
print(solution(word))