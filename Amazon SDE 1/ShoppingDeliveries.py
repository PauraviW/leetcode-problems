def getMinTime(buildingOpenTime,offloadTime):

    buildingOpenTime.sort()

    offloadTime.sort(reverse=True)

    i = 0
    j = 0
    count = 0
    t = 0
    maxv = 0

    while i < len(buildingOpenTime):

        while j < len(offloadTime) and count != 4:
            t = buildingOpenTime[i] + offloadTime[j]
            maxv = max(t, maxv)
            count+=1
            j+=1

        count = 0
        i += 1


    return maxv

print(getMinTime([8, 10],[2,2,3,1,8,7,4,5]))