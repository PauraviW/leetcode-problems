class Solution:
    def queensAttacktheKing(self, queens: [[]], king: []) -> [[]]:
        i, j = king
        l = []
        # same row before kings position
        while j >= 0:
            if [i,j] in queens:
                l.append([i, j])
                queens.remove([i, j])
                break
            j -=1
        j = king[1]
        # same row after kings position
        while j < 8:
            if [i, j] in queens:
                l.append([i, j])
                queens.remove([i, j])
                break
            j += 1

        i, j = king
        # same column before kings position
        while i >= 0:
            if [i, j] in queens:
                l.append([i, j])
                queens.remove([i, j])

                break
            i -= 1
        i = king[0]
        # same column after kings position
        while i < 8:
            if [i, j] in queens:
                l.append([i, j])
                queens.remove([i, j])

                break
            i += 1
        i, j = king
        # diagonal before
        while i >= 0 and j >= 0:
            if [i, j] in queens:
                l.append([i, j])
                queens.remove([i, j])

                break
            i -= 1
            j -= 1
        i, j = king
        # diagonal before
        while i < 8  and j < 8:
            if [i, j] in queens:
                l.append([i, j])
                queens.remove([i, j])

                break
            i += 1
            j += 1

        i, j = king
        while i >= 0 and j < 8:
            if [i, j] in queens:
                l.append([i, j])
                queens.remove([i, j])

                break
            i -= 1
            j += 1
        i, j = king
        # diagonal before
        while i < 8  and j >= 0:
            if [i, j] in queens:
                l.append([i, j])
                queens.remove([i, j])

                break
            i += 1
            j -= 1

        return l

queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],
          [1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0]
    ,[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],
          [4,2],[1,0],
          [2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]

king = [3,4]
# print(Solution().queensAttacktheKing(queens, king))

qset = {(i, j) for i, j in queens}
## leetcode soluituon
ans = []
for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
        for k in range(1, 8):
            if (king[0] + i * k, king[1] + j * k) in qset:
                ans.append([king[0] + i * k, king[1] + j * k])
                break
