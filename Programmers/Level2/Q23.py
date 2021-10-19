# 조이스틱
def solution(name):
    answer = 0
    name = list(name)
    start = ['A' for _ in range(len(name))]

    idx = 0
    while start != name:
        if start[idx] != name[idx]:
            r = abs(ord(start[idx]) - ord(name[idx]))
            l = abs(ord(name[idx]) - ord('Z')) + 1
            answer += min(r, l)
            start[idx] = name[idx]
        else:
            r_idx = idx
            l_idx = idx
            for r_n in range(1, len(name)):
                if r_idx == len(name) - 1:
                    r_idx = 0
                else: r_idx += 1
                if start[r_idx] != name[r_idx]: break
            for l_n in range(1, len(name)):
                if l_idx == 0:
                    l_idx = len(name) - 1
                else: l_idx -= 1
                if start[l_idx] != name[l_idx]: break
            mov, idx = sorted([(r_n, r_idx),(l_n, l_idx)])[0]
            answer += mov

    return answer

name = "BBABAAAB"

print(solution(name))