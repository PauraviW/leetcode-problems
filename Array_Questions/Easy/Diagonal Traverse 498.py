from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, matrix: [[int]]) -> [int]:
        d = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                d[i+j].append(matrix[i][j])
        result = []
        for i in sorted(d.keys()):
            if i%2 == 0:

                rev = d[i]
                result += rev[::-1]
            else:
                result += d[i]
        print(result)


matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(Solution().findDiagonalOrder(matrix))