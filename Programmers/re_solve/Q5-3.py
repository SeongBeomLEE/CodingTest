def solution(brown, yellow):
    col = 3
    total = brown + yellow
    while True:
        if total % col == 0:
            row = total // col
            yellow_col = col - 2
            yellow_row = row - 2
            if yellow == yellow_col * yellow_row:
                if col >= row: break

        col += 1
    answer = [col, row]
    return answer