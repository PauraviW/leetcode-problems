import numpy as np

class Solution:
    def diagonalSort(self, mat: [[]]) -> [[]]:

        # row = 0
        # col = 0
        # m = np.shape(mat)[0]
        # n = np.shape(mat)[1]
        # l = []
        # while row >= col and row < m:
        #     ll = []
        #     i = row
        #     j = col
        #     while i < m and j < n:
        #         ll.append(mat[i][j])
        #         i += 1
        #         j += 1
        #     ll.sort()
        #     i = row
        #     j = col
        #     k = 0
        #     while i < m and j < n:
        #         mat[i][j] = ll[k]
        #         i += 1
        #         j += 1
        #         k += 1
        #     row +=1
        #     col = 0
        # row = 0
        # col = row + 1
        # while col < n and col > row:
        #     i = row
        #     j = col
        #     ll = []
        #     while j < n and i < m:
        #         ll.append(mat[i][j])
        #         j += 1
        #         i += 1
        #
        #     ll.sort()
        #     i = row
        #     j = col
        #     k = 0
        #     while j < n and i < m:
        #         mat[i][j] = ll[k]
        #         j += 1
        #         i += 1
        #         k += 1
        #     col += 1
        #     row = 0
        # return mat
        d = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i - j not in d:
                    d[i - j] = [mat[i][j]]
                else:
                    d[i - j].append(mat[i][j])
        for i in d:
            d[i].sort()

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                mat[i][j] = d[i - j][0]
                d[i - j].pop(0)
        return mat
    

mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
mat = [[37,98,82,45,42]]
mat = [[58],[99],[1],[6],[73],[9],[60],[88],[64],[60],[39],[29],[46],[20],[78],[95],[2],[35],[20],[53],[60],[15],[94],[78],[26],[89],[87],[93],[70],[31],[94],[58],[90],[48],[60],[6],[68],[62],[32],[36],[73],[49],[45],[31],[23],[3],[73],[70],[71],[18],[14],[49],[84],[72],[59],[91],[17],[46],[93],[31],[31],[71],[52],[83],[8],[95],[49],[57],[52],[65],[83],[98],[46],[55],[44],[100],[45],[7],[59],[38],[82],[62],[25],[55],[64],[56],[89],[2],[10],[57],[26],[19],[27],[80],[12],[32],[62],[91],[68],[92]]
print(Solution().diagonalSort(mat))