from collections import deque
def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    cnt = 0
    answer = []
    while progresses:
        if progresses[0] >= 100:
            cnt += 1
            progresses.popleft()
            speeds.popleft()
        else:
            if cnt != 0:
                answer.append(cnt)
                cnt = 0
            for idx in range(len(progresses)):
                progresses[idx] += speeds[idx]
    if cnt != 0:
        answer.append(cnt)
    return answer