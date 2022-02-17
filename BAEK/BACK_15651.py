# N과 M
N, M = map(int, input().split())
arr = [1] * M
idx = 0
while True:
    print(" ".join(list(map(str, arr[::-1]))))
    if sum(arr) == N * M: break
    arr[idx] += 1
    while arr[idx] > N:
        arr[idx] = 1
        idx += 1
        arr[idx] += 1
    idx = 0