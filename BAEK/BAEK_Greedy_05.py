# 아이디어
# 1. 전체 city를 하나씩 움직일 때 마다 최소의 기름 값을 구한다.
# 2. 그 기를 값으로 나머지 키로를 구하면 그 값이 최소의 기름 값이 된다.
# 3. 중요한 것은 첫번째가 최소의 기름 값일 가능성이 있기 때문에 그 조건을 추가해준다.

N = int(input())
km = list(map(int,input().split()))
city = list(map(int,input().split()))
min_cost = max(city)

total = 0
for i in range(N-1):
    if i == 0:
        total += city[i] * km[i]
        min_cost = min(min_cost, city[i])
    else:
        min_cost = min(min_cost, city[i])
        total += min_cost * km[i]

print(total)