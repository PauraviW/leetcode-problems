class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        rows = matrix
        columns = []
        for i in range(len(matrix[0])):
            l = []
            for j in range(len(matrix)):
                l.append(matrix[j][i])
            columns.append(l)
        print(columns)

        i = 0
        j = 0
         

matrix = [
  [1, 2, 3, 4, 13, 14],
  [5, 6, 7, 8, 15, 16],
  [9,10,11,12, 17, 18],
  [19, 20, 21, 22, 23, 29],
  [24, 25, 26, 27, 28, 30]
]
print(Solution().spiralOrder(matrix))

