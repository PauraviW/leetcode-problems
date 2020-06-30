class Solution:
    def sortString(self, s: str) -> str:
        # L = len(s)
        # k = ''
        #
        # while len(k) < L:
        #     j = ''
        #     asc_set = set(s)
        #     j += ''.join(sorted(asc_set))
        #     for i in j:
        #         s = s.replace(i,'',1)
        #     l = ''
        #     desc_set = set(s)
        #     l = ''.join(sorted(desc_set, reverse = True))
        #     for i in l:
        #         s = s.replace(i, '',1)
        #     k +=  j + l
        # return k
        raw = {i: s.count(i) for i in set(s)}
        seq = sorted(raw.keys())
        out = ""
        while sum(raw.values()) > 0:
            for i in seq:
                if raw[i] > 0:
                    out += i
                    raw[i] -= 1
            for i in seq[::-1]:
                if raw[i] > 0:
                    out += i
                    raw[i] -= 1
        return out






s = "aaaabbbbcccc"
s = 'leetcode'
s = 'rat'
s = 'gggggg'
s = 'spo'
print(Solution().sortString(s))