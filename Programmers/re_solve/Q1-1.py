def solution(participant, completion):
    player_dic = {}
    answer = ''

    for p in participant:
        if p not in player_dic:
            player_dic[p] = 1
        else:
            player_dic[p] += 1
    for c in completion:
        player_dic[c] -= 1

    for p, cnt in player_dic.items():
        if cnt >= 1:
            answer += p
            break

    return answer