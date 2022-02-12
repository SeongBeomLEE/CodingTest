# 일곱 난쟁이
from collections import deque

arr = []
for _ in range(9):
    arr.append(int(input()))

def solution(arr):
    for a in arr:
        q = deque([[a]])
        while q:
            val_li = q.popleft()
            if len(val_li) == 7:
                if sum(val_li) == 100:
                    return sorted(val_li)
                else:
                    continue
            if len(val_li) < 7:
                for i in arr:
                    if i not in val_li:
                        q.append(val_li[:] + [i])

answer = solution(arr)
for i in answer:
    print(i)
