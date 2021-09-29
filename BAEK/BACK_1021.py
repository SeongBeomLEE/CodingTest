# 회전하는 큐
n, m = map(int, input().split())
s_li = list(map(int, input().split()))
q = [i for i in range(1, n + 1)]
cnt = 0

for s in s_li:
    q_len = len(q)
    q_idx = q.index(s)
    # 앞쪽이 더 까가운 경우
    if q_idx < q_len - q_idx:
        while True:
            if q[0] == s:
                del q[0]
                break
            else:
                q.append(q[0])
                del q[0]
                cnt += 1
    # 뒤쪽이 더 가까운 경우
    else:
        while True:
            if q[0] == s:
                del q[0]
                break
            else:
                q.insert(0, q[-1])
                del q[-1]
                cnt += 1
print(cnt)

