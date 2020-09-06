coins = [1, 2, 5, 10]
sum = 27
array = []
i = 0
def number_of_ways(coins, sum):
    array = [[1] + ([0]*sum) for i in range(len(coins))]

    for i in range(1,sum+1):
        if i % coins[0] == 0:
            array[0][i] = 1
    for coin_value in range(1,len(array)):
        for cost in range(1, len(array[0])):
            if coins[coin_value] > cost:
                array[coin_value][cost] = array[coin_value-1][cost]
            else:
                diff = cost - coins[coin_value]
                array[coin_value][cost] = array[coin_value-1][cost] +  array[coin_value][diff]

    return array[-1][-1]
print("Number of ways", number_of_ways(coins, sum))

def number_of_coins(coins, sum):
    # array = [[0] * (sum+1) for i in range(len(coins))]
    #
    # for i in range(len(coins)):
    #     for j in range(len(array[0])):
    #         if j == 0:
    #             array[i][j] = 0
    #         elif i == 0:
    #             if j % coins[i] == 0:
    #                 array[i][j] = int(j/coins[i])
    #         elif coins[i] > j:
    #             array[i][j] = array[i-1][j]
    #         else:
    #             min_prev = array[i-1][j]
    #             array[i][j] = min(min_prev, 1 + array[i][j-coins[i]])
    # return array[-1][-1]
    array = [[float("inf")] * (sum + 1) for i in range(len(coins))]
    for j in range(sum + 1):
        array[0][j] = float("inf")
    for i in range(len(coins)):

        for j in range(sum+1):
            if j == 0:
                array[i][j] = 0
            elif coins[i] > j:
                array[i][j] = array[i - 1][j]
            else:
                array[i][j] = min(array[i - 1][j], 1 + array[i][j - coins[i]])
    return array[-1][-1] if array[-1][-1] >=0 else -1


sum = 10
coins  = [2,6, 5]
print(number_of_coins(coins, sum))





