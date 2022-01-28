# 추억의 2048게임
'''

- 각 변수의 좌표가 존재하는 dict를 생성한다,
- a(작은 값),b(큰 값) 의 좌표를 오른쪽 왼쪽 기준으로 나누어 생각해야함
- a가 b의 왼쪽에 있을 때는 단순 수학으로 계산 가능
- a가 b의 오른쪽에 있을 때는 조건을 나누어 계산해여함

'''

T = int(input())
for test_case in range(1, T + 1):
    a, b = input().split()
    a, b = int(a), int(b)
    if b < a:
        a, b = b, a

    # 좌표 찾기
    n, n_dict, total_cnt, cnt, x, y = b + 1, {}, 1, 0, 0, 0
    for i in range(1, n + 1):
        n_dict[i] = [x, y]
        cnt += 1
        y += 1
        if cnt == total_cnt:
            x += 1
            total_cnt += 1
            y, cnt = 0, 0

    # 최소 거리 찾기
    x1, y1 = n_dict[a]
    x2, y2 = n_dict[b]
    dis = 0
    # a가 b의 왼쪽에 있을 때
    if x1 <= x2 and y1 <= y2:
        dis = max(abs(x1 - x2), abs(y1 - y2))
    # a가 b의 오른쪽에 있을 때
    else:
        while True:
            if x1 == x2 and y1 == y2: break

            # 같은 y축라인에 있을 때
            if x1 == x2:
                dis += y2 - y1
                x1, y1 = x2, y2

            # 왼쪽을 기준으로 x 축에 같은 라인에 있을 때
            elif y1 == y2:
                dis += x2 - x1
                x1, y1 = x2, y2

            # 오른쪽을 기준으로 x 축에 같은 라인에 있을 때
            elif (x2 - x1) == (y2 - y2):
                dis += x2 - x1
                x1, y1 = x2, y2

            else:
                dis += y1 - y2
                y1 = y2

    print(f'#{test_case} {dis}')



