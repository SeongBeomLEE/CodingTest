# 예산
def solution(d, budget):
    d.sort()
    answer = 0
    for dd in d:
        budget -= dd
        if budget < 0 : break
        answer += 1
    return answer
d = [1,3,2,5,4]
budget = 9
print(solution(d, budget))