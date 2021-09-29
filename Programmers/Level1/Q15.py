# 실패율
def solution(N, stages):
    len_play = len(stages)
    answer = []
    for n in range(N):
        cnt = stages.count(n + 1)
        if cnt != 0:
            answer.append([n + 1, cnt / len_play])
            len_play -= cnt
        else:
            answer.append([n + 1, 0])
    answer = sorted(answer, key = lambda x: x[1], reverse = True)
    return [idx[0] for idx in answer]

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))