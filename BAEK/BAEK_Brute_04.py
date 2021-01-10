# M이 가로 , N이 세로
def solution(ex):
    chass_W = ["W" if i % 2 == 0 else "B" for i in range(8)]
    chass_B = ["B" if i % 2 == 0 else "W" for i in range(8)]

    count_li = []
    count_W = 0
    count_B = 0
    for idx, li in enumerate(ex):
        if idx % 2 == 0:
            for x, y in zip(chass_W, li):
                if x != y:
                    count_W += 1
            for x, y in zip(chass_B, li):
                if x != y:
                    count_B += 1
        else:
            for x, y in zip(chass_B, li):
                if x != y:
                    count_W += 1
            for x, y in zip(chass_W, li):
                if x != y:
                    count_B += 1

    count_li.append(count_W)
    count_li.append(count_B)
    return min(count_li)

M, N = map(int,input().split())

chass_list = []
for _ in range(M):
    chass_list.append(list(input()))

# 중요 아이디어
# 8칸씩 짤라서 모든 판을 탐색
result = []
for i in range(M - 7):
    for j in range(N - 7):
        ex = [c[(0+j):(8+j)]for c in chass_list[(0+i):(8+i)]]
        result.append(solution(ex))
print(min(result))
