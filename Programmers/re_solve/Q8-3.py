'''
1. 변경된 단어
2. 단어 방문 여부
3. 변경 횟수
'''
from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words: return answer
    visited = [True] * len(words)
    cnt = 0
    # 가로 2개 넣어야 하는 것 꼭 집중
    q = deque([[begin, visited, cnt]])
    while q:
        now_word, visited, cnt = q.popleft()
        if now_word == target:
            return cnt
        for idx, change_word in enumerate(words):
            if visited[idx]:
                word_cnt = 0
                for nw, cw in zip(now_word, change_word):
                    if nw != cw:
                        word_cnt += 1
                    if word_cnt > 1:
                        break
                else:
                    if word_cnt == 1:
                        _visited = visited[:]
                        _visited[idx] = False
                        q.append([change_word, _visited, cnt + 1])