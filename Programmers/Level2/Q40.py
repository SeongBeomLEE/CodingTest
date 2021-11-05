# 구명보트
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while len(people) >= 2:
        answer += 1
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else: people.pop()
    answer += len(people)
    return answer
people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))
