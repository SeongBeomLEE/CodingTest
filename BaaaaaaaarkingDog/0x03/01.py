# https://www.acmicpc.net/problem/10808
# 알파벳 개수

def solution(input : str):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    alphabet_to_index = {alphabet:index for index, alphabet in enumerate(alphabet_list)}

    answer = [0] * len(alphabet_list)

    for s in input:
        answer[alphabet_to_index[s]] += 1
    
    answer = list(map(str, answer))

    return " ".join(answer)

input_string = input()
print(solution(input_string))

