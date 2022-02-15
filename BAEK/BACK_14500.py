# 테트로미노

def up_down_symmetry(arr):
    rows, cols = len(arr), len(arr[0])
    new_arr = []
    for row in range(rows - 1, -1, -1):
        _new_arr = []
        for col in range(cols):
            _new_arr.append(arr[row][col])
        new_arr.append(_new_arr)
    return new_arr

def left_right_symmetry(arr):
    rows, cols = len(arr), len(arr[0])
    new_arr = []
    for row in range(rows):
        _new_arr = []
        for col in range(cols - 1, -1, -1):
            _new_arr.append(arr[row][col])
        new_arr.append(_new_arr)
    return new_arr

def transpose(arr):
    rows, cols = len(arr), len(arr[0])
    new_arr = []
    for col in range(cols):
        _new_arr = []
        for row in range(rows):
            _new_arr.append(arr[row][col])
        new_arr.append(_new_arr)
    return new_arr

def get_a(arr):
    '''
    ____
    '''
    answer = 0
    rows, cols = len(arr), len(arr[0])
    for row in range(rows):
        for col in range(0, cols - 4 + 1):
            val = arr[row][col] + arr[row][col + 1] + arr[row][col + 2] + arr[row][col + 3]
            answer = max(answer, val)

    return answer

def get_b(arr):
    '''
    __
    __
    '''
    answer = 0
    rows, cols = len(arr), len(arr[0])
    for row in range(0, rows - 2 + 1):
        for col in range(0, cols - 2 + 1):
            val = arr[row][col] + arr[row + 1][col] + arr[row][col + 1] + arr[row + 1][col + 1]
            answer = max(answer, val)

    return answer

def get_c(arr):
    '''
    _
    _
    __
    '''
    answer = 0
    rows, cols = len(arr), len(arr[0])
    for row in range(0, rows - 3 + 1):
        for col in range(0, cols - 2 + 1):
            val = arr[row][col] + arr[row + 1][col] + arr[row + 2][col] + arr[row + 2][col + 1]
            answer = max(answer, val)

    return answer

def get_d(arr):
    '''
    _
    __
     _
    '''
    answer = 0
    rows, cols = len(arr), len(arr[0])
    for row in range(0, rows - 3 + 1):
        for col in range(0, cols - 2 + 1):
            val = arr[row][col] + arr[row + 1][col] + arr[row + 1][col + 1] + arr[row + 2][col + 1]
            answer = max(answer, val)

    return answer

def get_e(arr):
    '''
    ___
     _
    '''
    answer = 0
    rows, cols = len(arr), len(arr[0])
    for row in range(0, rows - 2 + 1):
        for col in range(0, cols - 3 + 1):
            val = arr[row][col] + arr[row][col + 1] + arr[row][col + 2] + arr[row + 1][col + 1]
            answer = max(answer, val)

    return answer

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0

answer = max(answer, get_a(arr), get_b(arr), get_c(arr), get_d(arr), get_e(arr))
# 상하
arr = up_down_symmetry(arr)
answer = max(answer, get_c(arr), get_d(arr), get_e(arr))

# 좌우
arr = left_right_symmetry(arr)
answer = max(answer, get_c(arr), get_d(arr))

# 상하
arr = up_down_symmetry(arr)
answer = max(answer, get_c(arr), get_d(arr))

# 복원
arr = left_right_symmetry(arr)

# 전치
arr = transpose(arr)
answer = max(answer, get_a(arr), get_b(arr), get_c(arr), get_d(arr), get_e(arr))

# 상하
arr = up_down_symmetry(arr)
answer = max(answer, get_c(arr), get_d(arr), get_e(arr))

# 좌우
arr = left_right_symmetry(arr)
answer = max(answer, get_c(arr), get_d(arr))

# 상하
arr = up_down_symmetry(arr)
answer = max(answer, get_c(arr), get_d(arr))

print(answer)