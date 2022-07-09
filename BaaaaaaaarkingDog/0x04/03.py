# https://www.acmicpc.net/problem/1158
# 요세푸스 문제

import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split(" "))

linked_list = {}

answer = []

for n in range(1, N + 1):
    if n == 1:
        linked_list[n] = [N, n + 1]
    elif n == N:
        linked_list[n] = [n - 1, 1]
    else:
        linked_list[n] = [n - 1, n + 1]

if N < linked_list[N][1]:
    answer = [1]
    
else:
    cnt = 1
    now = 1
    while linked_list:
        if cnt % K == 0:
            answer.append(now)
            prev, next = linked_list[now]
            linked_list[prev][1] = next
            linked_list[next][0] = prev
            del linked_list[now]
            now = next
            cnt += 1
        else:
            now = linked_list[now][1]
            cnt += 1

print("<" + ", ".join(list(map(str, answer))) + ">")