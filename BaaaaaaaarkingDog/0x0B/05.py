# https://www.acmicpc.net/problem/1780
# 종이의 개수
import sys
input = sys.stdin.readline
N = int(input())
papers = []
for _ in range(N):
    papers.append(input().rstrip().split(' '))

minus_one_paper_count = 0
zero_paper_count = 0
one_paper_count = 0

def solution(x, y, N):
    global minus_one_paper_count, zero_paper_count, one_paper_count
    
    check = papers[x][y]
    for dx in range(N):
        for dy in range(N):
            if check != papers[x + dx][y + dy]:
                for i in range(3):
                    for j in range(3):
                        solution(x + i * N // 3, y + j * N // 3, N // 3)
                return

    if check == '-1': minus_one_paper_count += 1
    if check == '0': zero_paper_count += 1
    if check == '1': one_paper_count += 1

solution(0, 0, N)

print(minus_one_paper_count)
print(zero_paper_count)
print(one_paper_count)