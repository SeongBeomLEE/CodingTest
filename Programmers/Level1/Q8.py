# 내적
def solution(a, b):
    answer = sum([i*j for i, j in zip(a, b)])
    return answer
a = [1,2,3,4]
b = [-3,-1,0,2]
print(solution(a, b))
