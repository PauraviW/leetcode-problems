from collections import defaultdict


class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        # d = defaultdict(list)
        # d[1] = [1,1]
        #
        # for i in range(2, row_index+1):
        #     temp = d[i-1]
        #     l = []
        #     for j in range(1, len(temp)):
        #         l.append(temp[j] + temp[j-1])
        #     d[i] += [1] + l + [1]
        # print(d)
        # return d[row_index]
        result = [1]
        for i in range(0, rowIndex):
            for j in range(i, 0, -1):
                result[j] = result[j] + result[j - 1]
            result.append(1)
        return result


row_index = 33
print(Solution().getRow(row_index))