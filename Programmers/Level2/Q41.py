# 피로도
from collections import deque
def solution(k, dungeons):
    answer = -1
    q = deque()
    for idx in range(0, len(dungeons)):
        q.append([idx, [], k, 0])
        while q:
            start, vis, _k, _cnt = q.popleft()
            answer = max(answer, _cnt)
            vis = list(vis) + [start]

            if dungeons[start][0] <= _k:
                __k = _k - dungeons[start][1]
                __cnt = _cnt + 1
                for _idx in range(0, len(dungeons)):
                    if _idx not in vis: q.append([_idx, vis, __k, __cnt])
                    else: answer = max(answer, __cnt)
            else:
                answer = max(answer, _cnt)

    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))

print(8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)