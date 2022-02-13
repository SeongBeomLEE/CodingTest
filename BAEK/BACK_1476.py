# 날짜계산
E, S, M = map(int, input().split())
year = 1
_E, _S, _M = year, year, year
while True:
    if E == _E and S == _S and M == _M: break
    year += 1
    _E += 1
    _S += 1
    _M += 1
    if _E == 16: _E = 1
    if _S == 29: _S = 1
    if _M == 20: _M = 1

print(year)

