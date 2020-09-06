def coinChanging(total, coins):
    matrix = [[0]*(total+1) for i in range(len(coins)+1)]
    print(matrix)

    for i in range(len(coins)+1):

        for j in range(total + 1):
            if i == 0 and j == 0:
                matrix[i][j] = 1
            else:
                if i > j:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-i]
    print(matrix)

money = 10
coins = [1, 5, 6, 9]
coinChanging(money, coins)

