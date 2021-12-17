'''
AAAAA

AAAAZ

이동은 앞 뒤로 가장 가까운 친구로
본 문제에 한해 오른쪽 먼저 움직이는 것이 최적해를 보장함

알파벳 이동은 위 아래 값중에 가장 작은 값으로
위로 올라가는 경우 ord('J') - ord('A')
아래로 내리는 경우 ord('Z') - ord('J') + 1


'''


def solution(name):
    name = list(name)
    initial_name = ['A'] * len(name)
    answer = 0
    idx = 0
    while name != initial_name:
        if name[idx] != initial_name[idx]:
            answer += min(ord(name[idx]) - ord('A'), ord('Z') - ord(name[idx]) + 1)
            initial_name[idx] = name[idx]
        else:
            l_idx = idx
            r_idx = idx
            for i in range(1, len(name)):
                l_idx -= 1
                r_idx += 1
                if l_idx < 0:
                    l_idx = len(name) - 1
                if r_idx >= len(name):
                    r_idx = 0

                if name[r_idx] != initial_name[r_idx]:
                    answer += i
                    idx = r_idx
                    break

                if name[l_idx] != initial_name[l_idx]:
                    answer += i
                    idx = l_idx
                    break

    return answer