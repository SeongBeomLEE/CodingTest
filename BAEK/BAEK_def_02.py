def d(a): # 생성자 생성
    n = 0 # 초기화
    new = list(str(a)) # ex) 12 -> '12' -> ['1' , '2']
    for i in new:
        n = n + int(i)

    return a + n

Constructor = [] # 생성자
self_number = [] # 셀프 넘버
for i in range(1, 10001):
    a = d(i)
    Constructor.append(a)

for i in range(1, 10001):
    if i in Constructor:
        pass
    else:
        self_number.append(i)

for i in self_number:
    print(i)