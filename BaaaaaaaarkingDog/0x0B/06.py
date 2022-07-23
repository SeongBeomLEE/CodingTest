# https://www.acmicpc.net/problem/2630
# 색종이 만들기
import sys
input = sys.stdin.readline
N = int(input())
papers = []
for _ in range(N):
    papers.append(input().rstrip().split(' '))

zero_paper_count = 0
one_paper_count = 0

def solution(x, y, N):
    global zero_paper_count, one_paper_count
    
    check = papers[x][y]
    for dx in range(N):
        for dy in range(N):
            if check != papers[x + dx][y + dy]:
                for i in range(2):
                    for j in range(2):
                        solution(x + i * N // 2, y + j * N // 2, N // 2)
                return

    if check == '0': zero_paper_count += 1
    if check == '1': one_paper_count += 1

solution(0, 0, N)

print(zero_paper_count)
print(one_paper_count)