# 최댓값과 최솟값
def solution(s):
    li = list(map(int, s.split(' ')))
    answer = f'{min(li)} {max(li)}'
    return answer
s = "1 2 3 4"
print(solution(s))