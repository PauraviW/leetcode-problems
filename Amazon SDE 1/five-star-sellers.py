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
    while currentSum < reqdSum:
        currentSum = 0
        maxContribution = 0
        productItem = -1
        for i in range(len(productRatings)):
            contribution = (productRatings[i][0] + 1) * 1.0 / (productRatings[i][1] + 1) - productRatings[i][0] * 1.0 / \
                           productRatings[i][1]
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

