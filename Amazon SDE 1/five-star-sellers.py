import math
def fiveStartReviews(productRatings, ratingsThreshold):
    totalProducts = len(productRatings)
    result = 0
    reqdSum = ratingsThreshold * totalProducts * 1.0 / 100
    currentThreshold = 0

    for i in range(len(productRatings)):
        currentThreshold += productRatings[i][0] / productRatings[i][1]

    currentThreshold /= totalProducts
    if currentThreshold * 100 >= ratingsThreshold:
        return 0
    currentSum = 0
    zero_contribution = set()
    while currentSum < reqdSum:
        currentSum = 0
        maxContribution = 0
        productItem = -1
        for i in range(len(productRatings)):
            if i not in zero_contribution:
                contribution = (productRatings[i][0] + 1) * 1.0 / (productRatings[i][1] + 1) - productRatings[i][0] * 1.0 / \
                               productRatings[i][1]
                if contribution == 0:
                    zero_contribution.add(i)
                if maxContribution < contribution:
                    maxContribution = contribution
                    productItem = i

            currentSum += productRatings[i][0] * 1.0 / productRatings[i][1]

        currentSum = currentSum - productRatings[productItem][0] * 1.0 / productRatings[productItem][1]
        productRatings[productItem][0] = productRatings[productItem][0] + 1
        productRatings[productItem][1] = productRatings[productItem][1] + 1
        currentSum = currentSum + productRatings[productItem][0] * 1.0 / productRatings[productItem][1]
        result += 1
    return result

print(fiveStartReviews([[4,4], [2,3], [3, 6]], 77))

"""
In this question, what I am trying to do is to find out how much more increase in the threshold is needed and choose amongst the items which item has the highest percentage of contribution.

"""
