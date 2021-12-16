from collections import deque
def solution(priorities, location):
    loc_li = [ idx for idx, _ in enumerate(priorities)]
    loc_li = deque(loc_li)
    priorities = deque(priorities)
    answer = 0
    while priorities:
        val = priorities.popleft()
        loc = loc_li.popleft()
        if not priorities :
            answer += 1
            break
        if val >= max(priorities):
            answer += 1
            if loc == location:
                break
        else:
            priorities.append(val)
            loc_li.append(loc)
    return answer