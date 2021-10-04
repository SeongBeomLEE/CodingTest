# 기능 개발
from collections import deque
def solution(progresses, speeds):
    week = 0
    cnt = 1
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while progresses:
        _week = week
        progresse = progresses.popleft()
        speed = speeds.popleft()
        while progresse + speed * week < 100:
            week += 1
        if _week == week:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer[1:]
progresses = [93, 30, 55]
speeds = [1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))