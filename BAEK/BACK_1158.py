# 요세푸스 문제
m = input().split(' ')
N, K = int(m[0]), int(m[1])
N_li = [str(i) for i in range(1, N + 1)]

answer = []
idx = -1
while N_li:
    for _ in range(K):
        idx += 1
        if idx == len(N_li): idx = 0
    answer.append(N_li.pop(idx))
    idx -= 1

print('<'+", ".join(answer)+'>')