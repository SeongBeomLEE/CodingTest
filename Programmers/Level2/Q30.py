# 방금그곡
def get_m(m):
    tem = ''
    m_li = []
    for _m in m:
        if _m != '#':
            if len(tem) == 1:
                m_li.append(tem)
                tem = ''
                tem += _m
            else: tem += _m
        else:
            m_li.append(tem + '#')
            tem = ''
    if len(tem) == 1: m_li.append(tem)
    return m_li

def solution(m, musicinfos):
    answer = []
    m = get_m(m)
    cnt = 1
    for mf in musicinfos:
        start, end, title, mf_m = mf.split(',')

        start_h, start_m = start.split(':')
        end_h, end_m = end.split(':')

        time = (int(end_h) * 60 + int(end_m)) - (int(start_h) * 60 + int(start_m))

        mf_m = get_m(mf_m)

        if time <= len(mf_m):
            mf_m = mf_m[:time]
        else:
            mod, n = divmod(time, len(mf_m))
            mf_m = (mf_m * mod) + mf_m[:n]

        if len(m) <= len(mf_m):
            for i in range(len(mf_m) - len(m) + 1):
                temp = 0
                _mf_m = mf_m[i:]
                for _m, _mf in zip(m, _mf_m[:len(m)]):
                    if _m == _mf: temp += 1

                if temp == len(m):
                    answer.append([time, cnt, title])
                    cnt += 1
                    break

    if answer: return sorted(answer, reverse = True, key = lambda x: (x[0], -x[1]))[0][2]
    else: return "(None)"

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))