s = input()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# 크로아티아 알파벳 개수
for i in croatia:
    s = s.replace(i,"*") # 제거 후에 크로아티아 알파벳 형태로 바뀌는 것을 방지

print(len(s))