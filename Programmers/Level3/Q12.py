# 단어 변환
def solution(begin, target, words):
    answer = 0
    if target not in words: return answer
    q = [[begin, answer]]
    while q:
        w, ans = q.pop(0)
        _ans = ans + 1
        for word in words:
            cnt = 0
            for w1, w2 in zip(w, word):
                if w1 != w2: cnt += 1
                if cnt > 1: break
            else:
                if cnt == 1:
                    if word == target:
                        return _ans
                    q.append([word, _ans])
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))