import math
def fiveStartReviews(productRatings, ratingsThreshold):
    totalProducts = len(productRatings)
    result = 0
    # this is the amount we need to add.
    reqdSum = ratingsThreshold * totalProducts * 1.0 / 100

    # if already the threshold is crossed then no need to process more
    currentThreshold = 0

    for i in range(len(productRatings)):
        currentThreshold += productRatings[i][0] / productRatings[i][1]

    currentThreshold /= totalProducts
    if currentThreshold * 100 >= ratingsThreshold:
        return 0
    currentSum = 0
    # when some reviews are 100% then we do not need to calculate them again and again as they are not going to help improve the answer
    zero_contribution = set()
    while currentSum < reqdSum:
        # we chekc for each iteration, what is the current sum and try to make it bigger than the required sum
        currentSum = 0
        # this is to track the max contribution of the product
        maxContribution = 0
        productItem = -1


        for i in range(len(productRatings)):
            # calculate only if this item helps in increasing the contribution
            if i not in zero_contribution:
                # check the current contribution by adding one five star review to the current item
                contribution = (productRatings[i][0] + 1) * 1.0 / (productRatings[i][1] + 1) - productRatings[i][0] * 1.0 / \
                               productRatings[i][1]
                # if it is 0 i.e 100 % reviews correct
                if contribution == 0:
                    zero_contribution.add(i)
                # if this items contribution is the highest then select it to be changed for this round
                if maxContribution < contribution:
                    maxContribution = contribution
                    productItem = i
            # calculate the current sum for each item
            currentSum += productRatings[i][0] * 1.0 / productRatings[i][1]
        # after identifying the item, remove its effect from the current sum
        currentSum = currentSum - productRatings[productItem][0] * 1.0 / productRatings[productItem][1]
        # add one item to the identified item
        productRatings[productItem][0] = productRatings[productItem][0] + 1
        productRatings[productItem][1] = productRatings[productItem][1] + 1
        # add its new contribution
        currentSum = currentSum + productRatings[productItem][0] * 1.0 / productRatings[productItem][1]
        # increase the result by one
        result += 1
    return result

print(fiveStartReviews([[4,4], [2,3], [3, 6]], 77))

"""
In this question, what I am trying to do is to find out how much more increase in the threshold is needed and choose amongst the items which item has the highest percentage of contribution. 
Time complexity: 


"""
