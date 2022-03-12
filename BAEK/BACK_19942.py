'''
다이어트
- 중복되는 idx를 지우는 것이 핵심
- 앞선 값들이 최소 비용을 만족하면 이 후에 반복은 진행하지 않아도 됨
- 마지막 idx 값을 기준으로 순환을 시작함으로써 최소 idx list를 얻을 수 있도록 함
'''

def get_answer(idx_list, p = 0, f = 0, s = 0, v = 0, cost = 0, start = 0):
    if min_val_list[0] <= p and min_val_list[1] <= f and min_val_list[2] <= s and min_val_list[3] <= v:
        answer.add((cost, tuple(idx_list)))
        return False
    for idx in range(start, N):
        if idx not in idx_list:
            get_answer(idx_list = idx_list[:] + [idx],
                       p = p + val_list[idx][0],
                       f = f + val_list[idx][1],
                       s = s + val_list[idx][2],
                       v = v + val_list[idx][3],
                       cost = cost + val_list[idx][4],
                       start = idx)

N = int(input())
min_val_list = list(map(int, input().split()))
val_list = []
for _ in range(N):
    val_list.append(list(map(int, input().split())))

answer = set()

for idx in range(N):
    get_answer(idx_list=[idx],
               p=val_list[idx][0],
               f=val_list[idx][1],
               s=val_list[idx][2],
               v=val_list[idx][3],
               cost=val_list[idx][4],
               start = idx)

if answer:
    answer = sorted(list(answer))[0]
    print(answer[0])
    print(' '.join(list(map(lambda x: str(int(x) + 1), answer[1]))))
else:
    print(-1)