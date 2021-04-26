# 괴도 예은
# 핵심아이디어
# 총 3가지를 뽑기 때문에 반복문은 3개를 돌린다.
# 반복문의 시작은 순서는
# 1. 0 ~ N - 2(끝 2개는 이후에 반목문에 값이기 때문에 추가하면 안됨)
# 2. 처음 반복문 값 + 1 ~ N - 1
# 3. 두번째 반복문 값 + 1 ~ N

N, M = map(int, input().split())
arr = list(map(int, input().split()))
total = []

for i in range(0, N-2):
    for j in range(i + 1, N - 1):
        for n in range(j + 1, N):
            res = arr[i] + arr[j] + arr[n]
            if res <= M:
                total.append(res)

print(max(total))


