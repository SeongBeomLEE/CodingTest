# 프린터
from collections import deque
def solution(priorities, location):
    priorities = deque([[i, idx] for idx, i in enumerate(priorities)])
    answer = []
    while priorities:
        temp = True
        j, idx = priorities.popleft()
        for i, _idx in priorities:
            if j < i:
                priorities.append([j, idx])
                temp = False
                break
        if temp:
            answer.append([j, idx])
    for cnt, (i, idx) in enumerate(answer):
        if idx == location: break
    return cnt + 1

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))

