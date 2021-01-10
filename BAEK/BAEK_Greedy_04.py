# 아이디어
# -를 제외하고 모든 숫자를 다 더한 후 빼주면 그 값이 언제나 최솟 값이다.
# -를 기준으로 숫자를 나눈다
# 나머지 숫자를 다 더해준 다음
# 첫번째 수에 순차적으로 모두 빼준다.

# eval 사용 불가
# 왜? 0 다음에 숫자가 오면 eval은 오류를 내보냄
li = input().split('-')
num = []
for i in li:
    count = 0
    s = i.split('+')
    for j in s:
        count += int(j)
    num.append(count)
result = num[0]
for i in range(1, len(num)):
    result -= num[i]
print(result)