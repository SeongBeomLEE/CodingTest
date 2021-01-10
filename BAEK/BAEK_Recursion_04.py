# 재귀함수의 활용법
# 하노이탑
# start = 출발기둥, end = 도착기둥, size=원판의 개수
def hanoi(start, end, size):
    # 원판이 1개라면 시작에서 끝으로 이동하면 종료
    if size == 1: return print(start, end)
    hanoi(start, 6-start-end, size-1)
    print(start, end)
    hanoi(6-start-end, end, size-1)

size = int(input())
print(2**size-1)
hanoi(1, 3, size)
