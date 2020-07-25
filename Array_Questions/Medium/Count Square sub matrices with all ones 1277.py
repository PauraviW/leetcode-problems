
def countSquares(A):
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1


    return sum(map(sum, A))


matrix =[[0,1,1,1],[1,1,1,1],[0,1,1,1]]
print(countSquares(matrix))