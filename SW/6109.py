# 추억의 2048게임
'''

- 0에 해당하는 값들을 옮기는 함수
- 2개씩 비교하면서 같이 똑같으면 더 한후 사라지는 함수
- 바뀐 후의 리스트, 바뀌기 전의 리스트의 모든 값을 비교한 후 같은지 다른지 판단하는 함수

'''
import copy

def change_maps_up(maps, N):
    maps = copy.deepcopy(maps)
    for i in range(N):
        for j in range(N):
            _i = i
            _j = j
            if maps[i][j] == 0:
                while 0 <= _j < N and 0 <= _i < N and maps[_i][_j] == 0:
                    _i += 1
                if 0 <= _j < N and 0 <= _i < N and maps[_i][_j] != 0:
                    maps[i][j], maps[_i][_j] = maps[_i][_j], 0

    return maps

def change_maps_down(maps, N):
    maps = copy.deepcopy(maps)
    for i in range(N - 1, -1, -1):
        for j in range(N):
            _i = i
            _j = j
            if maps[i][j] == 0:
                while 0 <= _j < N and 0 <= _i < N and maps[_i][_j] == 0:
                    _i -= 1
                if 0 <= _j < N and 0 <= _i < N and maps[_i][_j] != 0:
                    maps[i][j], maps[_i][_j] = maps[_i][_j], 0

    return maps

def change_maps_left(maps, N):
    maps = copy.deepcopy(maps)
    for j in range(N):
        for i in range(N):
            _i = i
            _j = j
            if maps[i][j] == 0:
                while 0 <= _j < N and 0 <= _i < N and maps[_i][_j] == 0:
                    _j += 1
                if 0 <= _j < N and 0 <= _i < N and maps[_i][_j] != 0:
                    maps[i][j], maps[_i][_j] = maps[_i][_j], 0

    return maps

def change_maps_right(maps, N):
    maps = copy.deepcopy(maps)
    for j in range(N - 1, -1, -1):
        for i in range(N):
            _i = i
            _j = j
            if maps[i][j] == 0:
                while 0 <= _j < N and 0 <= _i < N and maps[_i][_j] == 0:
                    _j -= 1
                if 0 <= _j < N and 0 <= _i < N and maps[_i][_j] != 0:
                    maps[i][j], maps[_i][_j] = maps[_i][_j], 0

    return maps

def val_compare_up(maps, N):
    maps = copy.deepcopy(maps)
    for i in range(N - 1):
        for j in range(N):
            if maps[i][j] == maps[i + 1][j]:
                maps[i][j], maps[i + 1][j] = maps[i][j] + maps[i + 1][j], 0

    return maps

def val_compare_down(maps, N):
    maps = copy.deepcopy(maps)
    for i in range(N - 1, 0, -1):
        for j in range(N):
            if maps[i][j] == maps[i - 1][j]:
                maps[i][j], maps[i - 1][j] = maps[i][j] + maps[i - 1][j], 0

    return maps


def val_compare_left(maps, N):
    maps = copy.deepcopy(maps)
    for j in range(N - 1):
        for i in range(N):
            if maps[i][j] == maps[i][j + 1]:
                maps[i][j], maps[i][j + 1] = maps[i][j] + maps[i][j + 1], 0

    return maps

def val_compare_right(maps, N):
    maps = copy.deepcopy(maps)
    for j in range(N - 1, 0, -1):
        for i in range(N):
            if maps[i][j] == maps[i][j - 1]:
                maps[i][j], maps[i][j - 1] = maps[i][j] + maps[i][j - 1], 0

    return maps

def compare_maps(befor_maps, now_maps):
    answer = False
    for befor_map, now_map in zip(befor_maps, now_maps):
        for i, j in zip(befor_map, now_map):
            if i != j:
                answer = True
            if answer: break
        if answer: break

    return answer

T = int(input())
for test_case in range(1, T + 1):
    N, command = input().split()
    N = int(N)
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    if command == 'up':
        maps = change_maps_up(maps, N)
        maps = val_compare_up(maps, N)
        maps = change_maps_up(maps, N)

    elif command == 'down':
        maps = change_maps_down(maps, N)
        maps = val_compare_down(maps, N)
        maps = change_maps_down(maps, N)

    elif command == 'right':
        maps = change_maps_right(maps, N)
        maps = val_compare_right(maps, N)
        maps = change_maps_right(maps, N)

    else:
        maps = change_maps_left(maps, N)
        maps = val_compare_left(maps, N)
        maps = change_maps_left(maps, N)

    print(f'#{test_case}')
    for m in maps:
        print(' '.join(list(map(str, m))))