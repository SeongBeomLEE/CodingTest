# 양궁대회
from collections import deque
def solution(n, info):
    answer = {}
    lion_win_info = [i + 1 for i in info]

    apeach_win_idx_li = [idx for idx, i in enumerate(info) if i != 0]
    total_apeach_win_score = 0
    for apeach_win_idx in apeach_win_idx_li:
        total_apeach_win_score += (10 - apeach_win_idx)

    for start_idx in range(11):
        if start_idx in apeach_win_idx_li:
            now_apeach_win_score = total_apeach_win_score - (10 - start_idx)
        else:
            now_apeach_win_score = total_apeach_win_score
        now_lion_win_score = 10 - start_idx
        _n = n - lion_win_info[start_idx]
        q = deque([[[start_idx], _n, now_lion_win_score, now_apeach_win_score]])

        while q:
            now_idx_li, now_n, lion_score, apeach_score = q.popleft()
            if now_n >= 0 and apeach_score < lion_score:
                if lion_score - apeach_score in answer:
                    answer[lion_score - apeach_score] += [now_idx_li]
                else:
                    answer[lion_score - apeach_score] = [now_idx_li]
            for idx in range(now_idx_li[-1] + 1, 11):
                if now_n - lion_win_info[idx] >= 0:
                    next_lion_score = lion_score + (10 - idx)
                    if idx in apeach_win_idx_li:
                        next_apeach_score = apeach_score - (10 - idx)
                    else:
                        next_apeach_score = apeach_score
                    q.append([now_idx_li[:] + [idx], now_n - lion_win_info[idx], next_lion_score, next_apeach_score])

    if answer:
        max_score = max(list(answer.keys()))
        max_score_li = sorted(answer[max_score], key = lambda x : len(x))[-1]
        answer = [0 for i in range(11)]
        for idx in max_score_li:
            answer[idx] = lion_win_info[idx]
            n = n - lion_win_info[idx]
        answer[10] = n
    else:
        answer = [-1]
    return answer

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(n, info))