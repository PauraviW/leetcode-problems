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