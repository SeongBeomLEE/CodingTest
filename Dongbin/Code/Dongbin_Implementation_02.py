# N = int(input())
N = 5
H = [i for i in range(N+1)]
M = [i for i in range(0, 60)]
S = [i for i in range(0, 60)]
count = 0
for h in H:
    for m in M:
        for s in S:
            result = str(h)+"시"+ str(m) +"분" + str(s) +"초"
            if "3" in result:
                count += 1
print(count)

'''
# 책에 있는 방법

# N = int(input())
N = 5
count = 0
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) + str(m) + str(s): count += 1
print(count)
'''


