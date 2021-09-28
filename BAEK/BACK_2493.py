# 탑
import sys
n = int(sys.stdin.readline())
top_li = list(map(int, sys.stdin.readline().split()))
stack = []
loc_li = []

for i in range(n):
    while stack:
        if stack[-1][1] > top_li[i]:
            loc_li.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        loc_li.append(0)
    stack.append([i, top_li[i]])
print(" ".join(map(str, loc_li)))

# while top_li:
#     top = top_li.pop()
#     _top_li = list(top_li)
#     loc = len(_top_li)
#     while _top_li:
#         _top = _top_li.pop()
#         if _top > top:
#             loc_li.append(str(loc))
#             break
#         else: loc -= 1
#     if loc == 0: loc_li.append(str(loc))
#
# print(' '.join(list(reversed(loc_li))))



