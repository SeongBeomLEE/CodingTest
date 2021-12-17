'''
최대 2명씩 탑승이기 때문에

가장 무거운 사람과 가장 가벼운 사람들만 고려한다.

'''
from collections import deque
def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    while people:
        answer += 1
        if len(people) > 1:
            if people[0] + people[-1] <= limit:
                people.popleft()
                people.pop()
            else:
                people.pop()
        else:
            people.pop()
    return answer