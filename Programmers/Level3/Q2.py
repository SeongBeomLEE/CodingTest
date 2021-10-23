# 자물쇠와 열쇠
# https://shoark7.github.io/programming/algorithm/rotate-2d-array
def rot(key, M):
    _key = [[0 for _ in i]for i in key]
    for row in range(M):
        for col in range(M):
            _key[col][M - 1 - row] = key[row][col]
    return _key

def pad(lock, N):
    new_lock = []
    idx = 0
    for i in range(N * 3):
        if i < N:
            new_lock.append([0] * N * 3)
        elif i < N * 2:
            new_lock.append([0] * N + lock[idx] + [0] * N)
            idx += 1
        else:
            new_lock.append([0] * N * 3)
    return new_lock

def solution(key, lock):
    M = len(key)
    N = len(lock)
    answer = False

    for i in range(4):
        if i != 0 :
            key = rot(key, M)
        x, y = 0, 0
        while True:
            if x > 3 * N - M: break
            new_lock = pad(lock, N)
            for row in range(M):
                for col in range(M):
                    new_lock[x + row][y + col] += key[row][col]

            y += 1
            if y > 3 * N - M:
                x += 1
                y = 0

            answer_li = []
            for row in range(N, N*2):
                answer_li += new_lock[row][N : N*2]

            if 0 not in answer_li:
                if 2 not in answer_li:
                    answer = True
                    break

        if answer: break

    return answer

# 키를 회전시킨다 (4번만 가능)
# 락을 넓힌다
# 락 부분 안에 1만 존재하면 트루를 반환한다

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))