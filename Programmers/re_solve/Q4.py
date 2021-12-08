# 단어 변환
def solution(begin, target, words):
    answer = 0
    vis = [False] * len(words)
    q = [[begin, answer, vis]]
    while q:
        now_word, cnt, vis = q.pop(0)
        if now_word == target:
            answer = cnt
            break

        cnt = cnt + 1
        for idx, next_word in enumerate(words):
            if not vis[idx]:
                w_cnt = 0
                for w1, w2 in zip(now_word, next_word):
                    if w1 != w2:
                        w_cnt += 1
                    if w_cnt > 1: break
                if w_cnt == 1:
                    _vis = vis[:]
                    _vis[idx] = True
                    q.append([next_word, cnt, _vis])
    else: answer = 0

    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))