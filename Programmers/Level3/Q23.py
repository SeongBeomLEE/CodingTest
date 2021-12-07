# 표 편집
# Linked list
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