def canStopRecusive(runway, initSpeed, startIndex=0):

    if startIndex >= len(runway) or startIndex < 0 or initSpeed < 0 or not runway[startIndex]:
        return False

    if initSpeed == 0:
        return True

    for adjustedSpeed in [initSpeed, initSpeed - 1, initSpeed + 1]:

        if canStopRecusive(runway, adjustedSpeed, startIndex + adjustedSpeed):
            return  True
    return  False

runway = [True] * 2 + [False] * 2 + [True] * 2 + [False] + [True] * 4
initSpeed = 5
print(canStopRecusive(runway, initSpeed))