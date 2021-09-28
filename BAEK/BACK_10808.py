# import string
# s_idx = {}
# for idx, s in enumerate(string.ascii_lowercase):
#     s_idx[s] = idx
#
# ss = input()
# ret = [0 for _ in range(len(s_idx))]
# for s in ss:
#     ret[s_idx[s]] += 1
#
# print(" ".join(str(i) for i in ret))

# 효율적
ss = input()
ret = [0] * 26
for s in ss:
    ret[ord(s) - ord('a')] += 1
print(" ".join(str(i) for i in ret))