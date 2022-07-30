# https://www.acmicpc.net/problem/14719
# 빗물
import sys
input = sys.stdin.readline

H, W = map(int, input().split(' '))
blocks = list(map(int, input().split(' ')))
answer = 0
max_block = max(blocks)
max_block_index = 0
for index in range(len(blocks)):
    if max_block == blocks[index]: 
        max_block_index = index

def serch(blocks):
    global answer
    right_max_block = max(blocks)
    right_max_block_index = 0
    for index in range(len(blocks)):
        if max_block == blocks[index]: 
            right_max_block_index = index

    while right_max_block_index != 0:
        left_max_block = max(blocks[:right_max_block_index])
        for index in range(len(blocks)):
            if left_max_block == blocks[index]:
                left_max_block_index = index
                break
        length = (right_max_block_index - left_max_block_index - 1)
        if length >= 1:
            answer += (length * left_max_block) - sum(blocks[left_max_block_index + 1: right_max_block_index])
        right_max_block_index = left_max_block_index

# 왼쪽 탐색
serch(blocks[:max_block_index + 1])
# 오른쪽 탐색
serch(blocks[max_block_index:][::-1])
print(answer)