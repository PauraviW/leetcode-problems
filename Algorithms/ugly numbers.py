import math
def logb(a,  b) :
    return 0 if a == 0 else math.log(a) / math.log(b);


def getIdealNums(low, high) :

    y = 0;

    maxY = math.floor(logb(high, 5));
    count = 0;
    while y <= maxY:
        exp = math.pow(5, y)
 
        min = math.ceil(logb(low / exp, 3));
        max = math.floor(logb(high / exp, 3));

        if (min <= max) :
            count += max-min+1;
        y += 1



    return count
print(getIdealNums(200, 405))

