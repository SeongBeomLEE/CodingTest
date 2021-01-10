# 1단계 몇번째 칸인지 찾는다
# 2단계 홀수번째 인지 짝수번째 인지 찾는다
# 3단계 위에서 시작하는 수와 아래에서 시작하는 수를 교차한다
# 짝수 번째는 위가 작은 값 부터 시작 / 아래가 큰 값부터 시작
# 홀수 번째는 위가 큰 값 부터 시작 / 아래가 작은 값부터 시작
def solution(input_num):
    n = 0
    max_num = 0
    while input_num > max_num:
        n += 1
        max_num += n

    gap = max_num - input_num
    if n % 2 == 0:
        up = n - gap
        dowun = gap + 1
    else:
        up = gap + 1
        dowun = n - gap

    return up, dowun

up, dowun = solution(int(input()))
print('{}/{}'.format(up, dowun))
