# 30
# 각 자릿수를 다 더했을 때 3의 배수가 나오면 30의 배수임
def solution(x):
    if 0 not in x : return -1
    if sum(x) % 3 == 0: return "".join(list(map(str, x)))
    else: return -1

x = sorted(list(map(int, list(input()))), reverse = True)
print(solution(x))

