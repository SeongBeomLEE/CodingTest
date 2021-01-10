# 1이 될 때까지
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# N이 1이 될 때까지 1번 혹은 2번 과정을 수행하는 최솟회수를 구한다.

# 아이디어
# 말 그대로 구현하는 것이 최고
# 횟수를 줄이기 위해서 1씩 뻬는 것이 아님 한번에 다 제거하는 것이 좋음
N, K = 29, 5
count = 0
while N >= K:
    while N % K != 0:
        N -= 1
        count += 1
    N //= K
    count +=1

# 최종적으로 K로 나누어지지 않는 N을 모두 제거함
count += (N - 1)
print(count)



