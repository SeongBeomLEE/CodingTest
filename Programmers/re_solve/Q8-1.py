'''
-1 +1
   -1

1  +1
   -1
'''
from collections import deque
def solution(numbers, target):
    answer = 0
    ret_cnt = len(numbers)
    q = deque([[0, 0]])
    while q:
        val, cnt = q.popleft()
        if cnt == ret_cnt:
            if val == target:
                answer += 1
            continue
        pos_val = val + numbers[cnt]
        neg_val = val - numbers[cnt]
        q.append([pos_val, cnt + 1])
        q.append([neg_val, cnt + 1])
    return answer