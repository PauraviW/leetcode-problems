import math


def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """

    i = 0
    timer = False

    while i < len(averageUtil):
        #
        if averageUtil[i] < 25:
            if instances > 1:
                instances = math.ceil(instances / 2)
                timer = True
        elif averageUtil[i] > 75:
            if instances * 2 <= 2 * 10 ** 8:
                instances = instances * 2
                timer = True

        if timer:
            i = i + 11
            timer = False
        else:
            i += 1
    return instances

# print(finalInstances(2, [25, 23, 1, 2, 3, 4 ,  5 ,  6 ,  7 ,  8 ,  9 ,  10 ,  76 ,  80 ]))
print(finalInstances(1, [5 , 10, 80 ]))
print(finalInstances(100000000, [  30  ,   95  ,   4  ,   8  ,   19  ,   89  ]))

# Time Complexity - O(n)
# Space Complexity - O(1)


"""
In this question, I go through every time stamp and check for the load at each instance. IF the load is below 25, i check if the number of instances is greater than one and then only divide the instances
else if the load is above 75 i check if doubling the instances does not cause an overflow and accordingly change it. 
I use a timer flag to track if we need to check the next instance or not. IF a timer flag is added, then i skip the next 10 values else i chekc all the instances. Toggling of flag is handled accordingly. 

"""