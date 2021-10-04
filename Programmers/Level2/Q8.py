# 짝지어 제거하기
from collections import deque
def solution(s):
    answer = 1
    s = deque(list(s))
    stack = []
    stack.append(s.popleft())
    while s:
        if stack and stack[-1] == s[0]:
            stack.pop()
            s.popleft()
        else:
            stack.append(s.popleft())
    if stack:
        answer = 0
    return answer

s = 'baabaa'
s = 'cdcd'
# print(s[:0] + s[2:])
print(solution(s))