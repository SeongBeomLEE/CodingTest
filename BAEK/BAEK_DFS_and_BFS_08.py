from collections import deque

# N은 시작 위치 K은 도착 위치
N, K = map(int,input().split())

# 방문했다면 Fasle
# 방문하지 않았다면 True
visit = [True] * 100001

def bfs(n):
    # 카운트를 시작
    count = 0
    q = deque()
    q.append((n, count))

    # 최단 거리의 경우
    # 결국 반복문 중에서 가장 먼저 끝난 값이 해답임
    # q가 다 사라질 때까지 반복
    # 하지만 사실상 q가 다 사라질 가능성은 전혀 없음
    while q:
        # BFS 방법을 사용 (선입 선출)
        # 가장 먼저 들어온 값들이 제일 중요한 값들임
        n, count = q.popleft()

        # True 방문하지 않았다면 조건문 실행
        if visit[n]:
            # 이미 방분했기 때문에 False
            visit[n] = False

            # 해답에 가장 먼저 도달한 값이 결국 해답임
            if n == K : return count

            # 방문을 했기 때문에 카운트 +1
            count += 1

            # 순간이동
            # n*2의 위치의 값일 경우 해당 답안이 가장 먼저 도달함
            if (n * 2) <= 100000:
                q.append((n*2, count))
            # 앞으로 이동
            # 앞으로 1칸 이동의 경우 해당 답안이 가장 먼저 도달함
            if (n + 1) <= 100000:
                q.append((n+1, count))
            # 뒤로 이동
            # 뒤로 1칸 이동의 경우 해당 답안이 가장 먼저 도달함
            if (n - 1) >= 0:
                q.append((n-1 , count))

print(bfs(N))