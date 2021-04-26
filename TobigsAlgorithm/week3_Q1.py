# 엿팔아요
# 핵심 아이디어
# 나머지가 없으면 구한 (몫 - 1) 만큼 짜른 비용을 대준다
# 나머지가 있으면 구한 몫 만큼 짜른 비용을 대준다
# 그리고 1부터 가장 큰 값 + 1 까지(가장 큰 값 자체가 최고의 경우의 수가 될 수도 있기 때문에) 모든 경우의룰 구한다.

N, C, F = map(int, input().split())
value_li = []
for _ in range(N):
    value_li.append(int(input()))

result_li = []
start = 1
while start < max(value_li) + 1:
    total = 0
    for i in value_li:
        if i % start == 0:
            # 공식을 알아내는 것 자체가 핵심
            total += ((i // start) * start * F) - ((i // start - 1) * C)
        else:
            total += ((i // start) * start * F) - ((i // start) * C)
    result_li.append(total)
    start += 1

print(max(result_li))


