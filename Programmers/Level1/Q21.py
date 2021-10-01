# 최소직사각형
def solution(sizes):
    w_li = []
    h_li = []
    for i in sizes:
        if i[1] <= i[0]:
            w_li.append(i[0])
            h_li.append(i[1])
        else:
            w_li.append(i[1])
            h_li.append(i[0])
    return max(w_li) * max(h_li)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes))