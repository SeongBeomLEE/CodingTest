s = input()
alpabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0
for idx, x in enumerate(alpabet):
    for i in x:
        time = time + s.count(i)*(idx+3)

print(time)

