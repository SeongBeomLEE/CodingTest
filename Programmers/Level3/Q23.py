# 표 편집
# Linked list
# 가정이 존재하기 때문에 가능한 방식임
# 1.표의 모든 행을 제거하여, 행이 하나도 남지 않는 경우는 입력으로 주어지지 않습니다.
# 2.표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.
# 3.원래대로 복구할 행이 없을 때(즉, 삭제된 행이 없을 때) "Z"가 명령어로 주어지는 경우는 없습니다.
def solution(n, k, cmd):
    # linked_list[k] = prev, next
    linked_list = {i : [i - 1, i + 1] for i in range(n)}
    del_link = []
    answer = ['O' for _ in range(n)]
    for situation in cmd:
        situation = situation.split(' ')
        if situation[0] == 'U':
            # 위로 이동
            for _ in range(int(situation[1])):
                k = linked_list[k][0]
        elif situation[0] == 'D':
            # 어래로 이동
            for _ in range(int(situation[1])):
                k = linked_list[k][1]
        elif situation[0] == 'C':
            # 삭제
            prev, next = linked_list[k]
            del_link.append([prev, next, k])
            answer[k] = 'X'

            # 삭제 후에 현재 행의 위치로 이동
            if next == n:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            # 연결리스트 변경
            if prev == -1:
                linked_list[next][0] = prev
            elif next == n:
                linked_list[prev][1] = next
            else:
                linked_list[next][0] = prev
                linked_list[prev][1] = next

        elif situation[0] == 'Z':
            # 복원
            prev, next, now = del_link.pop()
            answer[now] = 'O'

            # 연결리스트 복원
            if prev == -1:
                linked_list[next][0] = now
            elif next == n:
                linked_list[prev][1] = now
            else:
                linked_list[next][0] = now
                linked_list[prev][1] = now

        # print(situation)
        # print(linked_list)
        # print(del_link)
        # print(k)
        # print()

    return ''.join(answer)
n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))