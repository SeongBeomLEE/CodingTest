# 크레인 인형뽑기 게임
def solution(board, moves):
    basket = [0]
    answer = 0
    for x in moves:
        for y in range(0, len(board)):
            if board[y][x-1] != 0:
                cat = board[y][x-1]
                board[y][x - 1] = 0
                if basket[-1] == cat:
                    basket.pop(-1)
                    answer += 2
                else: basket.append(cat)
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))