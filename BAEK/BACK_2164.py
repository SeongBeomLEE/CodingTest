# 카드2
from collections import deque
que = deque([i for i in range(1, int(input()) + 1)])
while que:
    if len(que) != 1:
        head1 = que.popleft()
        head2 = que.popleft()
        que.append(head2)
    else:break

print(que[0])
