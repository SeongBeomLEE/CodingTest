# 영어 끝말잇기
from collections import deque
def solution(n, words):
    words = deque(words)
    out_words = []
    number = 1
    cnt = 1
    front = ''
    while words:
        word = words.popleft()
        if word in out_words: return [number, cnt]
        out_words.append(word)
        if front == '':
            front = word[0]
            back = word[-1]
        else:
            front = word[0]
            if back != front:
                return [number, cnt]
            back = word[-1]
        if number == n:
            number = 1
            cnt += 1
        else:
            number += 1
    answer = [0, 0]
    return answer
n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))