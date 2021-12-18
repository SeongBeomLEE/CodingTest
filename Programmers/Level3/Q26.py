# 최고의 집합
'''
n = 1 이면 그냥 s고
n = 2 이며 int(s / 2)
n = 3
13
4 3 6

7
6 3 4

'''

def solution(n, s):
    answer = []
    base = s // n
    rem = s % n
    if base == 0: return [-1]
    for _ in range(n - rem):
        answer.append(base)
    for _ in range(rem):
        answer.append(base + 1)
    return sorted(answer)