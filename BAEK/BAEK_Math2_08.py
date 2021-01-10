while True:
    li = list(map(int,input().split()))
    if li == [0, 0, 0]: break
    max_number = max(li)
    li.remove(max_number)
    if (((li[0]) ** 2 + (li[1]) ** 2) == (max_number) ** 2): print('right')
    else: print('wrong')
