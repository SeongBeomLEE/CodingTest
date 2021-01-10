def H(n):
    han = 0
    for i in range(1, n + 1):
        if i < 100:
            han += 1
        else:
            i_str_list = list(map(int, str(i)))
            if i_str_list[0] - i_str_list[1] == i_str_list[1] - i_str_list[2]:
                han += 1

    return han

n = int(input())
print(H(n))