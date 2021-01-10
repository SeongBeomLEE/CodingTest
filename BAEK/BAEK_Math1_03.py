# 6n의 등차수열 만큼 씩 값이 늘어남
# *으로 하면 시간복잡도가 늘어남 시간을 최소화 할 수 있는 방향으로 생각해야함
def solution(num):
    ret = 1
    n = 6
    first = 1
    if num == 1: return ret
    else:
        while True:
            first += n
            ret += 1
            if num <= first: return ret
            n += 6
num = int(input())
print(solution(num))