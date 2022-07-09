# https://www.acmicpc.net/problem/1406
# 에디터
# 연결리스트 풀이

import sys
input = sys.stdin.readline

node = list(input().rstrip())
start_index = 0
end_index = len(node) - 1

linked_list = {} # index : (prev_index, next_index)
for index in range(len(node)):
    if index == start_index:
        linked_list[index] = [None, index + 1]
    elif index == end_index:
        linked_list[index] = [index - 1, 'tail']
    else:
        linked_list[index] = [index - 1, index + 1]
        
linked_list['tail'] = [index, None]

n = int(input())

position = 'tail'

for _ in range(n):
    command = input().rstrip()
    now_index = position

    if command[0] == "P":
        node.append(command[2])
        node_index = len(node) - 1

        if linked_list[now_index][0] == None:
            linked_list[now_index][0] = node_index
            linked_list[node_index] = [None, now_index]
        else:
            now_linked_prev_index, now_linked_next_index = linked_list[now_index]
            prev_linked_prev_index, prev_linked_next_index = linked_list[now_linked_prev_index]
            
            linked_list[now_linked_prev_index][1] = node_index
            linked_list[now_index][0] = node_index

            linked_list[node_index] = [now_linked_prev_index, now_index]

    elif command[0] == "L":
        if linked_list[now_index][0] == None: continue
        else:
            position = linked_list[now_index][0]
    
    elif command[0] == "D":
        if linked_list[now_index][1] == None: continue
        else:
            position = linked_list[now_index][1]
    
    elif command[0] == "B":
        if linked_list[now_index][0] == None: continue
        else:
            now_linked_prev_index, now_linked_next_index = linked_list[now_index]
            prev_linked_prev_index, prev_linked_next_index = linked_list[now_linked_prev_index]
            
            linked_list[now_index][0] = prev_linked_prev_index
            if prev_linked_prev_index != None:
                linked_list[prev_linked_prev_index][1] = now_index

            del linked_list[now_linked_prev_index]

start_index = None
for index in linked_list.keys():
    if linked_list[index][0] == None:
        start_index = index
        break

answer = ""

while True:
    if start_index == 'tail': break
    answer += node[start_index]
    start_index = linked_list[start_index][1]

print(answer)
