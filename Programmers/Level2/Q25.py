# 예상 대진표
import math
def solution(n,a,b):
    answer = 0
    while abs(a - b) != 0:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1
    return answer
n = 8
a = 1
b = 2
print(solution(n,a,b))
