result = list(map(int,list(input())))
result.sort(reverse=True)
print("".join(list(map(str, result))))