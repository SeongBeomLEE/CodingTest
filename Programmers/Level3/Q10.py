# 단속카메라
from collections import deque
def solution(routes):
    answer = 0
    routes.sort()
    routes = deque(routes)
    start, end = routes.popleft()
    while routes:
        if start <= routes[0][0] and end >= routes[0][0]:
            start = routes[0][0]
            end = end if end <= routes[0][1] else routes[0][1]
            routes.popleft()
        else:
            answer += 1
            start, end = routes.popleft()
    answer += 1
    return answer
routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))