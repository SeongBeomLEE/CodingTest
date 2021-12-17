# 타겟 넘버
from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = [0, 0]
    q = deque([q])
    while q:
        print(q)
        s, cnt = q.popleft()
        if s == n:
            if cnt == target:
                answer += 1
            continue
        pos = cnt + numbers[s]
        neg = cnt - numbers[s]
        q.append([s + 1, pos])
        q.append([s + 1, neg])

    return answer
numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))