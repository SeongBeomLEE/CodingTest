# 아이디어
# 가장 돈을 뽑는데 걸리는 시간이 짧은 사람이 먼저 뽑는 것이 좋다.
# 1. 짧은 사람 순으로 나열한다.
# 2. 나열한 리스트를 각자 걸리는 시간을 구할 수 있도록 반복문을 돌린다.
# 3. 전체 시간을 다 더한 값을 출력한다.
N = int(input())
li = list(map(int,input().split()))
li.sort()
count = 0 # 각자 걸리는 시간
result = 0  # 전체가 걸리는 시간
for i in li:
    count += i
    result += count
print(result)